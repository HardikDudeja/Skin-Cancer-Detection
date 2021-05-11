

from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
# import ipynb
from cnn_model import *
from moleimages import *
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import matplotlib
from sklearn.metrics import confusion_matrix
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import sys
import seaborn as sns


# In[13]:


def plot_roc(y_test, y_score, title='ROC Curve'):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    print(roc_auc)
#     plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
#     plt.savefig(title + '.png')
    plt.show()
    


def run():
    sns.set()
    mimg = MoleImages()
    # X_test, y_test = mimg.load_test_images('data_scaled_validation/benign',
                                 # 'data_scaled_validation/malign/')

    X_test = mimg.run_test("../media/images")

    mycnn = CNN()
    model = load_model('mymodel-2_dosato.h5')

    y_pred_proba = model.predict(X_test)
    y_pred = (y_pred_proba >0.5)*1

    print(y_pred)
    # print(classification_report(y_test,y_pred))
    # plot_roc(y_test, y_pred_proba, title='ROC Curve CNN from scratch')
    # print(confusion_matrix(y_test, y_pred))

# In[5]:


# print(y_pred)


# In[ ]:




