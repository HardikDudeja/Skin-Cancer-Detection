from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import ipynb
from . import cnn_model as cn
from . import moleimages as mi
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import matplotlib
from sklearn.metrics import confusion_matrix
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import glob



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
    mimg = mi.MoleImages()


    X_test, X_name = mimg.run_test('/Users/hardikdudeja/Documents/PB_Project/PBproject/media/images')
    print(X_name)

    mycnn = cn.CNN()
    model = load_model('/Users/hardikdudeja/Documents/PB_Project/PBproject/main_app/mymodel-2_dosato.h5')

    y_pred_proba = model.predict(X_test)
    y_pred = (y_pred_proba >0.5)*1

    print(y_pred)

    return X_name, y_pred

def run_model2():
    sns.set()
    mimg = mi.MoleImages()


    X_test, X_name = mimg.run_test('/Users/hardikdudeja/Documents/PB_Project/PBproject/media/images')
    print(X_name)

    mycnn = cn.CNN()
    model = load_model('/Users/hardikdudeja/Documents/PB_Project/PBproject/main_app/mymodel-2.h5')

    y_pred_proba = model.predict(X_test)
    y_pred = (y_pred_proba >0.5)*1

    print(y_pred)

    return X_name, y_pred


def run_model3():
    sns.set()
    mimg = mi.MoleImages()


    X_test, X_name = mimg.run_test('/Users/hardikdudeja/Documents/PB_Project/PBproject/media/images')
    print(X_name)

    mycnn = cn.CNN()
    model = load_model('/Users/hardikdudeja/Documents/PB_Project/PBproject/main_app/mymodel.h5')

    y_pred_proba = model.predict(X_test)
    y_pred = (y_pred_proba >0.5)*1

    print(y_pred)

    return X_name, y_pred





