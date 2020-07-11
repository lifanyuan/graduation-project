import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def load_history(name):
    name = os.path.join('../history_plot', name)
    data = pd.read_csv(name)
    return data


history = load_history('MECDQNhistory.csv')
history_new = load_history('MECDQNhistorynew.csv')
h = history['episode_comrate']
h_mean = [np.mean(h[i:i + 10]) for i in range(len(h))]

new = history_new['episode_comrate'][0:180]
n_mean = [np.mean(new[i:i + 10]) for i in range(180)]
fig, ax = plt.subplots()
# plt.plot(h, label='parallel scheme', linestyle=':')
plt.plot(h_mean, label='parallel scheme')
# plt.plot(new, label='serial scheme', linestyle=':')
plt.plot(n_mean, label='serial scheme')
plt.xlabel('x-episodes')
plt.ylabel('y-computation rate')
plt.legend()

# ax.set_title('Episode_reward')
# ax.set_xlabel('episode')

# ax.plot(x, l)
# ax.set_title('Loss')
# ax.set_xlabel('episode')
plt.show()
