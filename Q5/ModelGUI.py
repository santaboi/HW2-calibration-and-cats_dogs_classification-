#random erasing source code :　https://github.com/zhunzhong07/Random-Erasing
import tkinter as tk
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
from tensorflow.keras import models
from tensorflow.keras.models import Sequential , load_model
import ssl
import os
from tensorflow.keras.preprocessing import image


#'dog': 1, 'cat': 0

#global input
inputValue = 0
root = tk.Tk()
root.title('E94081107 opencv HW2')
root.geometry('300x500')

def get_test_image(inputValue , wanted_file):
    img = image.load_img(wanted_file, target_size=(128, 128))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.       #rescale to (0-1)
    return img_tensor

def button_event1():
    print(model.summary())

def button_event2():
    print("this is a a model trained without any augmentation")
    tensorboard = cv2.imread("../Q5_data/img/tensorboard.png")
    cv2.imshow("The tensorboard result" , tensorboard)

def button_event3():
    global inputValue
    test_folder = "../Q5_data/test1/"
    wanted_file = os.path.join(test_folder , (str(inputValue) + ".jpg"))
    #print(wanted_file)
    output1 = model.predict(get_test_image(inputValue , wanted_file))
    output1_class = ""
    if np.argmax(output1, axis=None, out=None):
        output1_class = "dog"
    else:
        output1_class = "cat"
    #plot output
    test_sample = cv2.imread(wanted_file)
    fig1 = plt.figure("test img")
    plt.imshow(test_sample)
    plt.title("class :" + output1_class)
    plt.show()
        
    



def button_event4():
    print("compare a model1 to model2 ->model1 without any augmentation mode12 is only with random erasing")
    fig = plt.figure()
    model_names = ['without augmentation' , 'with augmentation']
    x = np.arange(len(model_names))
    #accuracy = [0.7884 , 0.7614]
    accuracy = [0.7614 , 0.7884]
    y = np.arange(len(accuracy))
    plt.bar(model_names, accuracy, color=['red','blue'])
    plt.xticks(x, model_names)
    plt.xlabel('model_names')
    plt.yticks(y , accuracy)
    plt.ylabel('acc')
    plt.title('random erasing vs without any aug')
    plt.show()


mybutton1 = tk.Button(root, text='1. Show Model Structure', command=button_event1)
mybutton1.pack()
mybutton2 = tk.Button(root, text='2. Show TensorBoard', command=button_event2)
mybutton2.pack()
#****input section****************************************************************
def retrieve_input():
    global inputValue 
    inputValue=textBox.get("1.0","end-1c")
    print("input for the model" , inputValue)

textBox=tk.Text(root, height=2, width=10)
textBox.pack()
buttonCommit=tk.Button(root, height=1, width=20, text="Commit_for_(3. Test)", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
#****input section****************************************************************
mybutton3 = tk.Button(root, text='3. Test', command=button_event3)
mybutton3.pack()
mybutton4 = tk.Button(root, text='4. Data Augmentation', command=button_event4)
mybutton4.pack()

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    #train_images,train_labels,test_images,test_labels = None
    os.environ['KMP_DUPLICATE_LIB_OK']='True'
    model = load_model("./model12-25.h5")
    root.mainloop()

    