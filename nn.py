import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


#=========================================================#
# Defining the class neural network. 
# Also its associate functions. 
#=========================================================#

class Net(nn.Module):

	def __init__(self):
		super(Net, self).__init__()
		self.conv1 = nn.Conv2d(1, 6, 3)
		self.conv2 = nn.Conv2d(6, 16, 3)

		self.fc1 = nn.Linear(16*6*6, 120)
		self.fc2 = nn.Linear(120, 84)
		self.fc3 = nn.Linear(84, 10)

	def forward(self, x):
		print(x.size())
		x = F.relu(self.conv1(x))
		print(x.size())
		x = F.max_pool2d(x, 2)
		print(x.size())
		x = F.relu(self.conv2(x))
		print(x.size())
		x = F.max_pool2d(x, 2)
		print(x.size())
		x = x.view(-1, self.num_flat_features(x))
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x

	def num_flat_features(self, x):
		size = x.size()[1:]
		num_features = 1
		for s in size:
			num_features *= s
		return num_features


#=========================================================#
# Defining an instance of class. 
#=========================================================#
net = Net()
print(net)
#=========================================================#

#=========================================================#
# Checking parameters of the model.
#=========================================================#
params = list(net.parameters())
print(len(params))
#=========================================================#


#=========================================================#
# Testing just on a sample input.
#=========================================================#
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)
#=========================================================#

#=========================================================#
# Setting the gradient to zero is very important.
#=========================================================#
net.zero_grad()
#=========================================================#

#=========================================================#
# BackProp.
#=========================================================#
net.zero_grad()
out.backward(torch.randn(1, 10))
#=========================================================#

#=========================================================#
# Loss Functions. 
#=========================================================#
output = net(input)
target = torch.randn(10)
target = target.view(1, -1)
criterion = nn.MSELoss()
loss = criterion(output, target)
#=========================================================#


#=========================================================#
# Calling BackPropogation with loss.
#=========================================================#
net.zero_grad()
loss.backward()
#=========================================================#

#=========================================================#
# Update the weights. 
#=========================================================#
learning_rate = 0.01
for f in net.parameters():
	f.data.sub_(f.grad.data * learning_rate)
#=========================================================#

#=========================================================#
# Using optimizers.
#=========================================================#
optimizer = optim.SGD(net.parameters(), lr=0.01)

optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()
#=========================================================#









