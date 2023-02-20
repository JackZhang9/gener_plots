import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
'''生成一个折线图和一个条状图'''


class chart_fig:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_excel(self.file)
        plt.figure()

    def spine_proce(self):
        ax = plt.gca()
        ax.spines['top'].set_color(None)
        ax.spines['right'].set_color(None)

    def x_y_ticks_proce(self, x_ticks, y_ticks):
        plt.xticks(x_ticks)
        plt.yticks(y_ticks, ['{}人'.format(int(i)) for i in y_ticks])

    def line_chart(self):  # 年度出生人口变化，按年分组，
        data_sub = self.data[['年份', '出生人数']].groupby('年份').sum()
        data_x = data_sub.index
        data_y = data_sub['出生人数']
        # plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(data_x, data_y, 'r-o', markersize=8, linewidth=3)
        x_ticks = np.arange(2018, 2023)
        y_ticks = plt.yticks()[0]
        self.x_y_ticks_proce(x_ticks, y_ticks)
        plt.ylabel('出生人数')
        plt.xlabel('年度')
        plt.title('年度出生人数变化趋势')
        self.spine_proce()

    def bar_chart(self):
        data_sub = self.data[['月份', '出生人数']].groupby('月份').sum()
        data_x = data_sub.index
        data_y = data_sub['出生人数']
        # plt.figure()
        plt.subplot(2, 1, 2)
        plt.bar(data_x, data_y)
        for x, y in zip(data_x, data_y):
            plt.text(x, y, y, ha='center', va='bottom')
        x_ticks = np.arange(1, 13)
        y_ticks = plt.yticks()[0]
        self.x_y_ticks_proce(x_ticks, y_ticks)
        plt.ylabel('出生人数')
        plt.xlabel('月份')
        plt.title('月度出生人数变化趋势')
        self.spine_proce()

    def fig_show(self):
        plt.show()


if __name__ == '__main__':
    file_name = '某地近五年每月出生人数.xls'
    chart_fig = chart_fig(file_name)
    chart_fig.line_chart()
    # chart_fig.fit_show()
    chart_fig.bar_chart()
    chart_fig.fig_show()





