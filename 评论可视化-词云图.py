import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def get_comments():
    with open('comments.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        comments = list()
        for comment in rows:
            try:
                comment = comment.split(',')[3]
                # print(comment)
            except:
                continue
            else:
                comments.append(comment)

        return comments

def get_word_cloud(comments):
    comments_after_aplit = jieba.cut(str(comments), cut_all=False)
    words = ' '.join(comments_after_aplit)
    # print(words)

    stopwords = STOPWORDS.copy()
    stopwords.add('哪吒')
    stopwords.add('电影')
    stopwords.add('我命')
    stopwords.add('不由')

    bg_img = plt.imread('circle.png')
    wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_img, stopwords=stopwords, max_font_size=200,
              random_state=50, font_path='STKAITI.TTF')
    wc.generate_from_text(words)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('词云图.jpg')


if __name__ == '__main__':
    get_word_cloud(get_comments())
