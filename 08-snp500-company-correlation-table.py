
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


style.use('ggplot')


def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    
    # draw plot from apple
    # df['AAPL'].plot()
    # plt.show()

    df_corr = df.corr()
    # print(df_corr.head())

    data = df_corr.values

    fig = plt.figure()
    # plot
    ax = fig.add_subplot(1, 1, 1)

    # set heatmap red/yellow/green
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)

    fig.colorbar(heatmap)

    # data.shape --> ( xaxis_data_counts , yaxis_data_counts)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

    # locate yaxis label to top
    ax.invert_yaxis()

    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)


    plt.xticks(rotation=90)

    # min max limit 정함
    heatmap.set_clim(-1, 1)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    visualize_data()

