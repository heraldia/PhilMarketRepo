# In [12]
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from pylab import *

def matrixP(alpha = ['A','B'],y_test = [0, 1],predicted_labels = [ 0.,  1.]):
# alpha = ['A','B']
# y_test = [0, 1]
#     alpha = ['bell','bus','flushing']
#     predicted_labels = [ 1., 0. , 2.,  0. , 0. , 0. , 1. , 1. , 0.,  0.]
#     y_test = [1, 0 ,2, 1, 1, 1, 1, 0, 1, 1]

    cm = confusion_matrix(y_test, predicted_labels)
    print y_test
    print predicted_labels
    fig = plt.figure()
    plt.clf()
    ax =  fig.add_subplot(111)
    ax.set_aspect(1)

    cax = ax.matshow(cm,cmap=plt.cm.jet, interpolation='nearest')


    for x in xrange(len(cm)):
        for y in xrange(len(cm[0])):
            ax.annotate(str(cm[y][x]),xy=(y,x),
                        horizontalalignment='center',
                        verticalalignment='center')

    _ = fig.colorbar(cax)



    ax.set_xticklabels(['']+alpha)
    ax.set_yticklabels(['']+alpha)

#     plt.title('Confusion matrix, single speaker')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
#     plt.show()
    plt.savefig('confusion_matrix.png', format='png')
    print cm

# matrixP()
