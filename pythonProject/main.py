import numpy as np
import matplotlib.pyplot as plt

# x=np.arange(0,np.pi,0.1)
# plt.plot(x,np.sin(x),'b')
# plt.plot(x,(x**2)/np.pi,'r')
# plt.plot(x,(x**2)/4,'g')
# plt.xlabel("x",fontsize=14)
# plt.ylabel('y',fontsize=14)
# plt.legend(['$y=sin(x)$','$y=(x^2)/pi$','$y=(x^2)/4$'],frameon=False)

x=[98,70,56,63,78]
label=['Class_A','Class_B','Class_C','Class_D','Class_E']
plt.title("")
e=(0,0,0.05,0.05,0)
plt.pie(x,labels=label,explode=e,autopct="%0.1f%%")
plt.show()
