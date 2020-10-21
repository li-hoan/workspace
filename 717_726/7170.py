from torchvision import datasets
from torchvision import transforms
from  torch.utils.data import DataLoader

#直接下载数据,在torchvision的datasets中
train=datasets.MNIST(root="",train=True,download=True,transform=transforms.ToTensor)#转换格式
test=datasets.MNIST(root="",train=False,download=False)
#
# img == train.data[0]
# u = transforms.ToPILImage()
# img = u(img)
# print(type(img))
# img.show()


train_loader = DataLoader(train_dataset,batch_size=100,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=100,shuffle=False)

