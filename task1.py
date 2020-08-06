import numpy
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x_data = [ 338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [ 640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# y_data = b + w * x_data
h_t = np.array([x_data,np.ones(len(x_data))])
h = np.transpose(h_t)
opt_w_b = (np.linalg.inv(h_t.dot(h))).dot(h_t.dot(y_data))  #least square estimation
print(opt_w_b)  # optimal w and b


# %%
x = np.arange(-200,-100,1) #bais
y = np.arange(-5,5,0.1) #weight
Z = np.zeros((len(x),len(y)))
X, Y = np.meshgrid(x,y)
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[j]
        Z[j][i] = 0
        for n in range(len(x_data)):
            Z[j][i] = Z[j][i] + (y_data[n] - b - w * x_data[n] )**2
        Z[j][i] = Z[j][i] / len(x_data)


# %%
# y_data = b + w * x_data
b = -120 #initial b
w = -4 #initial w
lr = 1 #learn rate
iteration = 100000

# store initial values for plotting
b_history = [b]
w_history = [w]

# AdaGrad
lr_b = 0
lr_w = 0

# iteration
for i in range(iteration):
    b_grad = 0.0
    w_grad = 0.0
    for n in range(len(x_data)):
        b_grad = b_grad -2.0*(y_data[n] - b - w*x_data[n])*1.0
        w_grad = w_grad -2.0*(y_data[n] - b - w*x_data[n])*x_data[n]

    lr_b = lr_b + b_grad**2
    lr_w = lr_w + w_grad**2
    # update parameters
    b = b - lr/np.sqrt(lr_b) * b_grad
    w = w - lr/np.sqrt(lr_w) * w_grad
    #store parameters for plotting
    b_history.append(b)
    w_history.append(w)

# plot the figure
plt.contour(x,y,Z,50,alpha=0.5,cmap=plt.get_cmap('jet'))
plt.plot(opt_w_b[1:2],opt_w_b[0:1],'x',ms=12,markeredgewidth=3,color='orange')
plt.plot(b_history,w_history,'o-',ms=3,lw=1.5,color='black')
plt.xlim(-200,-100)
plt.ylim(-5,5)
plt.xlabel(r'$b$',fontsize=16)
plt.ylabel(r'$w$',fontsize=16)
plt.show()
