import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def load_history(name):
    name = os.path.join('../history_plot', name)
    data = pd.read_csv(name)
    return data

def plot(history, key, window_length=10):
    h = history[key]
    h_mean = [np.mean(h[i:i + window_length]) for i in range(len(h))]
    # fig = plt.figure()
    # ax = fig.add_subplot(121)
    plt.plot(h, label='computation rate')
    plt.plot(h_mean, label='%d moving average' % window_length)
    plt.xlabel('x-episodes')
    plt.ylabel('y-computation rate')
    plt.legend()
    # ax.set_title('Episode_reward')
    # ax.set_xlabel('episode')
    # ax = fig.add_subplot(122)
    # ax.plot(x, l)
    # ax.set_title('Loss')
    # ax.set_xlabel('episode')
    plt.show()


history = load_history('MECDQNhistory.csv')

plot(history, 'episode_comrate')
