import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("E:\py\weibo_search_spider-master\jiangge.xlsx", "Sheet1")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(df['zhuanfa'],bins = 7)
plt.title = ('aaa')
plt.xlabel('zhuanfa')
plt.ylabel('#zhuanfashu')
plt.show()