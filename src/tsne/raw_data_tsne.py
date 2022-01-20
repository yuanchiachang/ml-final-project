import ast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.manifold import TSNE

NUM_DT = 22
NUM_DATA = 5000
PERPLEXITY = 150
DATA_PATH = "../lstm/data/dt_all.csv"
COLORS = ["steelblue", "red", "black", "brown", "yellow", "peachpuff", "cyan", "darkgray",
          "greenyellow", "hotpink", "lime", "magenta", "olivedrab", "orange", "blue", "peru"]

random.seed(420)
np.random.seed(420)

def load_data(df, train_dt, label_dt, num_data):
    train_dt = ["dt%d" % i for i in train_dt]
    label_dt = ["dt%d" % (label_dt - 1), "dt%d" % (label_dt)]
    label = df[label_dt].values.tolist()[:num_data]
    idx = df['chid'].tolist()[:num_data]
    tag_feat = df[train_dt].values.tolist()[:num_data]

    for i in range(len(tag_feat)):
        tag_feat[i] = np.array([ast.literal_eval(x) for x in tag_feat[i]]).reshape(-1)
    for i in range(len(label)):
        label[i][1] = np.array(ast.literal_eval(label[i][1]))

    return idx, tag_feat, [i[1] for i in label]

def draw_mix(data_embedded, targets):
    """
        draw all 16 classes in 2d

         - data_embedded: dimension-reduced (after TSNE) data
         - targets: class for that datapoint
    """

    color = np.array([COLORS[target] for target in targets])
    plt.scatter(data_embedded[:, 0], data_embedded[:, 1], s = 0.5, c = color)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    return

def draw_tag(data_embedded, targets, tag):
    """
        draw one specific class

         - data_embedded: dimension-reduced (after TSNE) data
         - targets: class for that datapoint
         - tag: class to draw
    """

    tag_embedded = data_embedded[targets == tag]
    plt.scatter(tag_embedded[:, 0], tag_embedded[:, 1], c = COLORS[tag])
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.show()

    return
 
def draw_each(data_embedded, targets):
    """
        draw the visualization result for each class in a 4 x 4 grid

         - data_embedded: dimension-reduced (after TSNE) data
         - targets: class for that datapoint
    """

    subplot_kw = {"xticks": [], "yticks": []}
    gridspec_kw = {"wspace": 0.1, "hspace": 0.2}
    fig, axs = plt.subplots(4, 4, gridspec_kw = gridspec_kw, subplot_kw = subplot_kw,
                            figsize = (12, 9))

    for tag in range(16):
        i = int(tag / 4)
        j = tag % 4
        axs[i, j].set_title(f"tag {tag}", {"fontsize": 6})
        tag_embedded = data_embedded[targets == tag]
        axs[i, j].scatter(tag_embedded[:, 0], tag_embedded[:, 1], s = 0.5, c = COLORS[tag])

    plt.show()

    return

def draw_chosen(data_embedded, targets, chosen):
    """
        draw some chosen classes in one graph

         - data_embedded: dimension-reduced (after TSNE) data
         - targets: class for that datapoint
         - chosen: list of classes to draw
    """
    chosen_embedded = []
    color = []

    for i in range(len(targets)):
        if (targets[i] in chosen):
            chosen_embedded.append(data_embedded[i])
            color.append(COLORS[targets[i]])

    chosen_embedded = np.array(chosen_embedded)
    color = np.array(color)

    plt.scatter(chosen_embedded[:, 0], chosen_embedded[:, 1], s = 0.5, c = color)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    return

if (__name__ == "__main__"):
    data = pd.read_csv(DATA_PATH)
    dt = [i for i in range(23 - NUM_DT, 23)]
    tsne = TSNE(n_components = 2, perplexity = PERPLEXITY, n_iter = 10000)
    chosen = [1, 2, 12, 13, 15]

    idx, feature, label = load_data(data, dt, 23, NUM_DATA)
    targets = np.argmax(label, axis = 1)
    data_embedded = tsne.fit_transform(feature)

    draw_mix(data_embedded, targets)
    draw_each(data_embedded, targets)
#     draw_chosen(data_embedded, targets, chosen)