'''
http://m.blog.csdn.net/blog/epsil_11109/9171527
'''
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def generateConfusionMatrix(conf_arr, alphabet):
    norm_conf = []
    for i in conf_arr:
        a = 0
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/(float(a)+0.000001))
        norm_conf.append(tmp_arr)
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    res = ax.imshow(np.array(norm_conf), cmap=plt.cm.jet,
                    interpolation='nearest')
    width = len(conf_arr)
    height = len(conf_arr[0])

    for x in xrange(width):
        for y in xrange(height):
            ax.annotate(str(conf_arr[x][y]), xy=(y, x),
                        horizontalalignment='center',
                        verticalalignment='center')
    cb = fig.colorbar(res)

    plt.xticks(fontsize=5)
    plt.yticks(fontsize=7)
    locs, labels = plt.xticks(range(width), alphabet[:width])
    for t in labels:
         t.set_rotation(90)
    #locs, labels = xticks([1,2,3,4], ['Frogs', 'Hogs', 'Bogs', 'Slogs'])
    #setp(alphabet, 'rotation', 'vertical')
    plt.yticks(range(height), alphabet[:height])
    plt.savefig('confusion_matrix.png', format='png')

if __name__ == '__main__':

    conf_arr=[
    [12,0,0,0,0,0,0],
    [0,12,0,0,0,0,0],
    [0,0,1,18,0,0,0],
    [0,0,0,9,0,0,3],
    [0,0,0,0,12,0,0],
    [0,0,0,0,0,10,0],
    [0,0,1,0,0,0,22],
    ];

    alphabet = \
     ['bell','cover','cutting','forkScratchBowl','putting','puttingCoverOnTable','stirEgg']
    generateConfusionMatrix(conf_arr, alphabet)
