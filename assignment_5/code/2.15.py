import matplotlib.pyplot as plt
x=range(-10,10)
y=[-i for i in x]
up=[10]*len(x)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)
plt.fill_between(x,y,up)
plt.show()
