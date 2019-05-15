#coding=utf-8


#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud,ImageColorGenerator
import  matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.analyse

content = open("whugoverjieba","rb").read()  #测试
#tags extraction based on TF-IDF algorithm
tags = jieba.analyse.extract_tags(content, topK=200, withWeight=False)
text =" ".join(tags)
print(text)
# text = unicode(text)

font=r'Songti.ttc'#
wordcloud=WordCloud(background_color='white',width=1000,max_font_size=100, height=1000,font_path=font,scale=3.5).generate(text)
  #img_color = ImageColorGenerator(self.img)

#显示词云

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('test.jpg')