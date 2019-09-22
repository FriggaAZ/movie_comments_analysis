from pyecharts import Pie

def get_score():
    with open("comments.txt", mode='r', encoding='utf-8') as f:
        all_comments = f.readlines()
        # print(all_comments)
        # count = 0
        sum = 0
        rates = list()
        for comment in all_comments:
            # count += 1
            try:
                score = comment.split(',')[4]
                # sum += float(score)
                # print(score)
                rates.append(score)
            except:
                continue

        print(rates)

        # avg_score = sum / count
        # print(sum)
        # print("平均分：" + str(avg_score))

    attr = ['五星', '四星', '三星', '二星', '一星']
    value = [
        rates.count('5') + rates.count('4.5'),
        rates.count('4') + rates.count('3.5'),
        rates.count('3') + rates.count('2.5'),
        rates.count('2') + rates.count('1.5'),
        rates.count('1') + rates.count('0.5'),
    ]

    pie = Pie("《哪吒》评分等级-饼图", title_pos='left', width=900)
    pie.add("", attr, value, is_label_show=True)
    pie.render("电影评分可视化-饼图.html")


if __name__ == '__main__':
    get_score()