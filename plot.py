from save import *
import matplotlib.pyplot as plt
from collections import Counter


def create_line_chart(data_sample, title, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    prices = (sorted(map(float, data_sample)))
    x_axis_ticks = list(range(len(data_sample)))
    ax.plot(x_axis_ticks, prices, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel('Tie Price ($)')
    ax.set_ylabel('Number of Ties')
    fig.savefig(exported_figure_filename)


def plot_all_bars(prices_in_float, exported_figure_filename):
    prices = list(map(int, prices_in_float))
    X = numpy.arange(len(prices))
    width = 0.25
    plt.bar(X + width, prices, width)
    plt.xlim([0, 5055])
    plt.savefig(exported_figure_filename)


def create_bar_chart(price_groups, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = plt.rcParams['axes.color_cycle']

    for group in price_groups:
        ax.bar(group, price_groups[group], color=colors[group % len(price_groups)])

    labels = ['$0-50', '$50-100', '$100-150', '$150-200', '$200-250', '$250+']
    ax.legend(labels)

    ax.set_title('Ties / Prices')
    ax.set_xlabel('Tie Price ($)')
    ax.set_ylabel('Number of Ties')
    ax.set_xticklabels(labels, ha='left')
    ax.set_xticks(range(1, len(price_groups) + 1))

    plt.grid(True)
    fig.savefig(exported_figure_filename)


def group_prices_by_range(prices_in_float):
    tally = Counter()
    for item in price_in_float:
        bucket = 0
        rounded_price = round(item, -1)


# create_line_chart([x[2] for x in gucci_ties[1:]], 'Price distribution for Gucci ties ', 'line_chart.png')

price_groups = group_prices_by_range(price_in_float)
create_bar_chart(price_groups, 'bar_chart.png')
