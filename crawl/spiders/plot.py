from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots()

y_pos=np.arange(4)
plot_value = [558, 414, 492, 375]
plot_label = ['careerbuilder','careerlink','timviecnhanh','vieclam24h']
rects = plt.bar(y_pos, plot_value, align='center', alpha=0.5 )
plt.xticks(y_pos, plot_label)
plt.ylabel('Number of files')
plt.title('Dataset')
for rect in rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%d' % height,
    ha='center', va='bottom')
# plt.show()