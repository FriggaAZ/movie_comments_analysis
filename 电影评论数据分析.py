from urllib import request
import json
from datetime import datetime, timedelta
import time

# 获取数据
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) \
        Version/11.0 Mobile/15A372 Safari/604.1'
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)

    if response.getcode() == 200:
        return response.read()


def parse_data(html):
    data = json.loads(html)['cmts']
    comments = list()
    for item in data:
        comment = {
            'id': item['id'],
            'nickName': item['nickName'],
            'cityName': item['cityName'] if 'cityName' in item else '',
            'content': item['content'].replace('\n', ' '),
            'score': item['score'],
            'startTime': item['startTime']
        }
        print(comment)
        comments.append(comment)
    return comments


def save_to_txt():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # start_time = '2019-08-17 12:31:34'
    end_time = '2019-07-26 08:00'
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset=0&startTime=' \
              + start_time.replace(' ', '%20')
        try:
            html = get_data(url)
        except:
            for i in range(10):
                time.sleep(0.3)
                html = get_data(url)
            print("服务器拒绝")
        else:
            time.sleep(0.05)
        comments = parse_data(html)
        start_time = comments[-1]['startTime']
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=1)
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

        for item in comments:
            with open('comments.txt', 'a', encoding='utf-8') as f:
                f.write(str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item['content'] + ','
                        + str(item['score']) + ',' + item['startTime'] + '\n')


if __name__ == '__main__':
    save_to_txt()
