import pandas as pd
import jieba
from collections import Counter
from pprint import pprint
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

# with open('S:/下载/呆萌的停用词表.txt','r',encoding='utf-8') as f:
#     stopwords = f.readlines()
# stoplist =[]
# for stopword in stopwords:
#     stoplist.append(stopword[:-1])
#
# df = pd.read_csv('D:/赚钱/sinaspider/sina/sina/spiders/xinguanbingdu.csv',encoding='gb18030')
# df['cut'] = df['txt'].astype(str).apply(lambda x:[i for i in jieba.cut(x) if i not in stoplist])
# df['cut'].to_csv('D:/赚钱/疫情分析/segword.csv',index=0)
wordall_str = ''
with open('D:/赚钱/疫情分析/segword.csv', 'r', encoding='utf-8-sig') as f:
    all = csv.reader(f)
    #wordall_list = []
    for words in all:
        words = words[0][1:-1].split(",")
        #print(len(words))
        for word in words:
            #print(word)
            wordall_str = wordall_str+" "+word

wc = WordCloud(font_path=r"C:/Windows/Fonts/simhei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(wordall_str)

plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()

wc.to_file('yiqing.png')
#counter = Counter(wordall)
#pprint(counter.most_common(30))