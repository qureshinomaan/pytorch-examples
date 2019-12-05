import torch
import numpy as np 

#=========================================================#
# Autograd looks cool. 
# Basically it remembers all the computation done on a 
# given tensor. And that really helps us backpropagate. 
#=========================================================#
#=========================================================#

#=========================================================#
# So lets start!
# We define x on which we would like to do some 
# computations. 
#=========================================================#
x = torch.ones(13, 1, requires_grad=True)
weights = torch.ones(1, 13, requires_grad = True)
print(x.requires_grad)
#=========================================================#

#=========================================================#
# Let's do some operations on x
# torch.mm is calculates dot product of two vectors. 
#=========================================================#
y = torch.mm(weights, x)
out = y
print(out)
#=========================================================#

#=========================================================#
# Now let's calculate d(out)/d(x)
# Note : grad can be calculated on scalar outputs only.
#=========================================================#
out.backward()
print(x.grad)
print(weights.grad)
#=========================================================#









