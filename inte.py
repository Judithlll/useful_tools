import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
import ode

def dfphdx(Y, x):
    phi,F = Y 
    dFdx = x**2*np.exp(-phi)
    dphidx = F/x**2
    return np.array([dphidx, dFdx])

y0=np.array([0.,0.]) #initial value of [phi, F]

x = np.array([0.001,15.])

sol = ode.ode(dfphdx, y0, x, 0.01, 'RK5')
xp = np.linspace(0.001,15.,1500)
plt.figure(dpi=1000)
plt.ylim(0,5)
plt.ylabel(r'$\phi = \Phi/c_s^2$')
plt.xlabel('$x=r/r_0$')
plt.plot(xp, sol[:,0] ,label='The solution')
plt.plot(xp, 1/6*xp**2, label = r'$\phi=\frac{1}{6} x^2$', color ='gray', alpha =0.3, linestyle ='dashed')
plt.legend()
plt.savefig('./phi~x.jpg')
plt.close()


#phi_s =np.array([])
#F_s = np.array([])
#for xs in np.linspace(1,100,1000):
#    sol = ode.ode(dfphdx, y0, np.array([0.001,xs]), 0.01, 'RK5')
    
#    phi_s = np.append(phi_s,sol[-1,0])
#    F_s =np.append(F_s, sol[-1,1])



