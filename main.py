import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sweetviz as sv

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 导入i3e数据
i3e_data = pd.read_csv('/Users/han/Desktop/Dissertation/i3e_data.csv')
# print(i3e_data.describe())

# plt.show()
print(i3e_data.describe())

'''
 plt.scatter(i3e_data['ΔТ, °C'], i3e_data['Т1, °C'],s=2)
 sns.scatterplot(i3e_data['ΔТ, °C'], i3e_data['Т1, °C'], s=2)
 sns.scatterplot(i3e_data['М1, t'], i3e_data['М2, t'], s=2)'''
sns.pairplot(i3e_data, diag_kind="kde", plot_kws=dict(s=2))
'''
my_report = sv.analyze(i3e_data)
my_report.show_html()
'''
plt.show()
