import jieba
import re
import matplotlib.pyplot as plt
import jieba.analyse
from wordcloud import WordCloud
from collections import Counter


class Lyric(object):

    def __init__(self, path):
        self.path = path

    def open_file(self):
        """打开文件"""
        with open(self.path, 'r') as f:
            content = re.sub(r'\n', "", f.read().encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))
        return content

    def load_stop_words(self):
        """读取停用词"""
        with open('stop_words.txt', 'r') as f:
            stop_words = f.read().split('\n')
        return stop_words

    def cut_lyric(self):
        """分词"""
        lyric = self.open_file()
        stop_words = self.load_stop_words()
        jieba.load_userdict('userdict.txt')
        lyric_generator = jieba.cut(lyric)
        lyric_list = [re.sub(r' ', "", l) for l in lyric_generator if l not in stop_words if l != ' ']
        tf_idf = jieba.analyse.tfidf(' '.join(lyric_list))
        print(tf_idf)
        return lyric_list

    def count_lyric(self, text_name):
        """词频统计"""
        lyric_list = self.cut_lyric()
        counter = Counter(lyric_list)
        count_pairs = counter.most_common(20)
        with open(text_name, 'w') as f:
            for c in count_pairs:
                print(c)
                f.write(c[0])
                f.write(' ')
                f.write(str(c[1]))
                f.writelines('\n')

    def word_cloud_plot(self, text, img):
        """绘制词云图"""
        path = 'pingfang.ttf'
        wordcloud = WordCloud(font_path=path,
                              background_color='black',
                              margin=1,
                              width=1368,
                              height=768,
                              max_words=200,
                              max_font_size=350)
        wordcloud = wordcloud.generate(text)
        wordcloud.to_file(img)
        plt.imshow(wordcloud)
        plt.axis('off')
        # plt.show()

    def show_word_cloud(self, img_name):
        """保存词云图"""
        text = ' '.join(self.cut_lyric())
        self.word_cloud_plot(text, img_name)


if __name__ == '__main__':
    print('------标题词频分析------')
    library_title = Lyric('library_text/title.txt')
    library_title.count_lyric('most_common/library_title/library_title_most_common_20.txt')
    library_title.show_word_cloud('word_cloud/title_cloud.jpg')
    print('------摘要词频分析------')
    library_description = Lyric('library_text/description.txt')
    library_description.count_lyric('most_common/library_description/library_description_most_common_20.txt')
    library_description.show_word_cloud('word_cloud/description_cloud.jpg')
    print('------内容词频分析------')
    library_content = Lyric('library_text/content.txt')
    library_content.count_lyric('most_common/library_content/library_content_most_common_20.txt')
    library_content.show_word_cloud('word_cloud/content_cloud.jpg')

