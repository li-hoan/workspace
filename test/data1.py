import os,torch,cv2
from torch.utils.data import Dataset
import numpy as np

class MNISTdata(Dataset):
    def __init__(self,root,is_train=True):
        self.data=[]
        if is_train==True:
            tt = "TRAIN"
        else:
            tt = "TEST"
        for tag in os.listdir(f"{root}/{tt}"):
            file_name  = f"{root}/{tt}/{tag}"
            for pic in os.listdir(file_name):
                pic_path = f"{file_name}/{pic}"
                self.data.append((pic_path,tag))
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        data = self.data[index]
        img = cv2.imread(data[0],cv2.IMREAD_GRAYSCALE)
        img_data =img.reshape(-1)
        img_data = img_data/255

        hot = np.zeros(10)
        hot[int(data[1])]=1

        return img_data,hot

if __name__ == '__main__':
    d = MNISTdata("data\MNIST_IMG")
    print(d[46000])