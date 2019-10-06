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
x = torch.ones(5, 3, requires_grad=True)
print(x.requires_grad)
#=========================================================#

#=========================================================#
# Let's do some operations on x
#=========================================================#
y = x + 2
y.requires_grad_(True)
z = y * y * y
out = z.mean()
print(z, out)
#=========================================================#

#=========================================================#
# Now let's calculate d(out)/d(x)
# Note : grad can be calculated on scalar outputs only.
#=========================================================#
out.backward()
print(y.grad)
#=========================================================#









