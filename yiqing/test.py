# -*- coding: utf-8 -*-

from wordcloud import WordCloud

import matplotlib.pyplot as plt

# 打开文本

text = open('xyj.txt',encoding="utf-8").read()

# 生成对象

wc = WordCloud(font_path='C:/Windows/Fonts/Inkfree.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)

# 显示词云

plt.imshow(wc, interpolation='bilinear')

plt.axis('off')

plt.show()

# 保存到文件

wc.to_file('wordcloud.png')  # 生成图像是透明的