import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_orders = pd.read_excel(r'C:\Users\user\Desktop\short.xlsx')
Data = df_orders






#опредляем координаты
x = df_orders['likes']
y = df_orders['views']

#seaborn


sns.lineplot(x = x, y = y)
plt.xlabel("views")
plt.ylabel("likes")
plt.title('Линейная диаграмма')
plt.show()




#matplotlib



fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("likes")
plt.ylabel("views")
plt.title('Линейная диаграмма')
plt.show()



#Диаграмма рассеивания
#матлаб
x1 = Data['likes']
x2 = Data['reposts']
y = Data['views']

fig, ax = plt.subplots()
plt.scatter(x1, y, label = 'likes')
plt.scatter(x2, y, label = 'reposts')

plt.legend()
plt.ylabel("views")
plt.title('Диаграмма рассеивания')
plt.show()


#Облако слов
from wordcloud import WordCloud
counter = 0


for i in Data['text']:
    try:
        text_length = len(i)
        if text_length > counter:
            counter = text_length
            text = i
    except:
        continue


wc = WordCloud(width=300, height=300, background_color="black")
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")

plt.show()
