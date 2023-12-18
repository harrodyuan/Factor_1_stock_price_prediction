# %% [markdown]
# ================
# ---
# # 因子实战 第一集 如何根据历史数据预测股价...?
# 
# ##### “人们从历史学到的唯一东西就是人类无法从历史学到任何东西” - 乔治·伯纳德·肖
# 
# ### [@大导演哈罗德](mailto:zhongfangyuan@link.cuhk.edu.cn)
# ### 香港中文大学深圳金融工程专业大四学生
# ### [Bilibili](https://space.bilibili.com/629573485)
# 
# 
# ---

# %% [markdown]
# 股票的每天的股价 跟之前的数据有没有关系？
# 
# ---
# 日内
# 
# ---
# 中短期
# 用昨天的股票数据预测今天的股票数据

# %%
import pandas as pd

# %%
data1 = pd.read_excel('16-17量价数据.xlsx')
data2 = pd.read_excel('18-19量价数据.xlsx')
data3 = pd.read_excel('20-21量价数据.xlsx')
data4 = pd.read_excel('2022量价数据.xlsx')

# %%
data1 = data1.drop(data1.index[0:2])
data2 = data2.drop(data2.index[0:2])
data3 = data3.drop(data3.index[0:2])
data4 = data4.drop(data4.index[0:2])

factor = pd.concat([data1, data2, data3, data4], axis=0)
factor = factor.sort_values(by= ["Symbol","TradingDate"])
factor

# %%
# 2016-2020日收益.xlsx
# 2016-2020流动率.xlsx
# 2021-2022日收益.xlsx
# 2021-2022流动率.xlsx
# 2016-2020日收益.xlsx
df1 = pd.read_excel('2016-2020日收益.xlsx')
df1 = df1.drop(df1.index[0])

df2 = pd.read_excel('2021-2022日收益.xlsx')
df2 = df2.drop(df2.index[0])

ret = pd.concat([df1, df2], axis=0)
ret = ret.sort_values(by= ["Stkcd","Trddt"])

ret

# %%
df3 = pd.read_excel('2016-2020流动率.xlsx')
df3 = df3.drop(df3.index[0:2])

df4 = pd.read_excel('2021-2022流动率.xlsx')
df4 = df4.drop(df4.index[0:2])

liq = pd.concat([df3, df4], axis=0)
liq = liq.sort_values(by= ["Stkcd","Trddt"])

liq

# %%
liq = liq.drop(columns=["Trddt",'Stkcd'])

liq

# %%
ret_reset = ret.reset_index(drop=True)
liq_reset = liq.reset_index(drop=True)
factor_reset = factor.reset_index(drop=True)

df = pd.concat([ret_reset, liq_reset, factor_reset], axis=1)

df = df.drop(columns=['TradingDate','Symbol','Status','SecurityID','PCF'])

df

# %%
X = df[['ILLIQ', 'PE', 'PB', 'PS', 'CirculatedMarketValue', 'ChangeRatio', 'Liquidility']]
y = df['Dretwd']


# %%
X

# %%
y

# %%
# 移动一天！！！！！！
y_shift = y.shift(-1)
y_shift

# %%
y_shift.fillna(method='ffill', inplace=True)
y_shift

# %% [markdown]
# # 用昨天的股票数据预测今天的股票数据涨跌幅
# # 我们已经有了完整的 数据集

# %%
X.to_csv('X.csv', index=False)
y_shift.to_csv('y.csv', index=False)


