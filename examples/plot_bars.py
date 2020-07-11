import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = [2, 3, 4, 5]
pure_v2v = [5.5195e8, 8.3924e8, 1.134e9, 1.434e9]
pure_v2i = [6.7918e8, 8.2381e8, 9.409e8, 1.0034e9]
serial = [7.893e8, 1.046e9, 1.311e9, 1.537e9]
parallel = [1.143e9, 1.416e9, 1.768e9, 1.924e9]

# x = np.arange(len(labels))  # the label locations
# width = 0.5 / 2  # the width of the bars
#
fig, ax = plt.subplots()
plt.plot(labels, pure_v2v, label='V2V only', marker='D')
plt.plot(labels, pure_v2i, label='V2I only', marker='D')
plt.plot(labels, serial, label='Serial', marker='D')
plt.plot(labels, parallel, label='Parallel', marker='D')
# rects1 = ax.bar(x -  width , pure_v2v, width, label='V2V only')
# rects2 = ax.bar(x , pure_v2i, width, label='V2I only')
# rects4 = ax.bar(x +  width , parallel, width, label='proposed')
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim(0, 2e9)
ax.set_ylabel('computation rate')
ax.set_xlabel('number of user and base vehicles')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
ax.legend()
#
# # def autolabel(rects):
# #     """Attach a text label above each bar in *rects*, displaying its height."""
# #     for rect in rects:
# #         height = rect.get_height()
# #         ax.annotate('{}'.format(height),
# #                     xy=(rect.get_x() + rect.get_width() / 2, height),
# #                     xytext=(0, 3),  # 3 points vertical offset
# #                     textcoords="offset points",
# #                     ha='center', va='bottom')
# #
# #
# # autolabel(rects1)
# # autolabel(rects2)
#
# fig.tight_layout()

plt.show()
