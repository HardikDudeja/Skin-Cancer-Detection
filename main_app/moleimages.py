#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import glob
import h5py
from PIL import Image


# In[3]:


class MoleImages:
    def __init__(self, path=None):
        self.path = path
        self.size = None
        
    
    def resize_bulk(self, size = (128,128)):
        self.size = size
        x = []
        image_list = glob.glob(self.path)
        num_images = len(image_list)
        print('Resizing {} images:'.format(num_images))
        for i, imgFile in enumerate(image_list):
            print('Resizing image {} of {}'.format(i+1, num_images))
            img = io.imread(imgFile)
            img = resize(img, self.size)
            x.append(img)
        
        return np.array(x)
    
    def load_test_images(self, dir_b, dir_m):
        X = []
        image_list_b = glob.glob(dir_b + '/*.png')
        n_images_b = len(image_list_b)
        print('Loading {} images of class benign:'.format(n_images_b))
        for i, imgfile in enumerate(image_list_b):
            print('Loading image {} of {}'.format(i+1, n_images_b))
            img = io.imread(imgfile)
            X.append(img)
        image_list_m = glob.glob(dir_m + '/*.png')
        n_images_m = len(image_list_m)
        print('Loading {} images of class malign:'.format(n_images_m))
        for i, imgfile in enumerate(image_list_m):
            print('Loading image {} of {}'.format(i+1, n_images_m))
            img = io.imread(imgfile)
            X.append(img)
        y = np.hstack((np.zeros(n_images_b), np.ones(n_images_m)))

        return np.array(X), y.reshape(len(y),1)
    
    def save_h5(self, x, filename, dataset):
        with h5py.File(filename, 'w') as hf:
            hf.create_dataset(dataset, data = x)
        
        print('File {} saved'.format(filename))
        
    def load_h5(self, filename, dataset):
        with h5py.File(filename, 'r') as hf:
             return hf[dataset][:]
            
    
    def save_png(self, matrix, dir, tag='img', format='png'):
        for i, img in enumerate(matrix):
            if dir[-1] != '/':
                filename = dir + '/' + tag + str(i) + '.' + format
            else:
                filename = dir + tag + str(i) + '.' + format
            print('Saving file {}'.format(filename))
            io.imsave(filename, img)


    def run_test(self, dir_image):
        size = (128,128)
        
        image_list = glob.glob(dir_image + '/*')
        n_images = len(image_list)
        print('number of images',n_images)
        print('Resizing {} images:'.format(n_images))
        for i, imgFile in enumerate(image_list):
            print('Resizing image {} of {}'.format(i+1, n_images))
            img = io.imread(imgFile)
            img = resize(img, size)
            io.imsave(imgFile, img)
        
        X = []
        X_name = []
        image_list = glob.glob(dir_image + '/*')
        # image_list = glob.glob(dir_image + '/*.png')
        print('Loading {} images for testing:'.format(n_images))
        for file in image_list:
            im = Image.open(file)
            X_name.append(im.filename)
        for i, imgfile in enumerate(image_list):
            print('Loading image {} of {}'.format(i+1, n_images))
            img = io.imread(imgfile)
            X.append(img)

        print(X_name)
        return np.array(X), np.array(X_name)
            
            
# if __name__ == '__main__':
#     benign = MoleImages('/Users/hardikdudeja/Documents/PB_Project/benign/*.jpg')
#     ben_images = benign.resize_bulk()
#     print('Shape of benign images: ', ben_images.shape)
#     benign.save_h5(ben_images, 'benigns.h5', 'benign')
        


# In[4]:


# images = MoleImages()


# In[5]:


# output = images.load_test_images('/Users/hardikdudeja/Documents/PB_Project/data_scaled/benign', '/Users/hardikdudeja/Documents/PB_Project/data_scaled/malign')


# In[ ]:




