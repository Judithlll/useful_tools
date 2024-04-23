import numpy as np
import math as m

"""
mainly wants to solve the ODE with multi-dimension initial conditions
"""
def RK5(fun_name,y0,t_span,step,*args):
    """
    fun_name: the name of the ODE to be solved like"fun_name(y0,t)"

    y0: ndarray, the initial value of the function at t=t_span[0]. and suggested shape of the y0 is the first dimension is the different particles, the second is different properties.

    t-span: the time span of the ODE to be solved like"[t_start, t_stop]"
    
    step: the step length of the t_span
    """
    ti=t_span[0]
    te=t_span[1]
    y=[]
    if abs(ti-te)<0.1:
        print('your tSpan is too small')
    
    n=1
    
    while ti<=te:
        # print(ti)
        k1=fun_name(y0,ti,*args)
        k2=fun_name(y0+step*k1/2,ti+step/2,*args)
        k3=fun_name(y0+step*k2/2,ti+step/2,*args)
        k4=fun_name(y0+step*k3,ti+step,*args)

        y1=y0+step/6*(k1+2*k2+2*k3+k4)
        # import pdb ; pdb.set_trace()
        if abs(y1.min()/y0.min())/step>100:
            print('warning: in the step ',[ti,ti+step],'too steep!! maybe you need a smaller step.')
        
        n+=1

        y.append(y0)
        
        y0=y1

        ti=ti+step
        
    #if n<=3:
    #    print('\r','maybe your step is too large!')

    y=np.array(y)
    
    return y

def Euler(fun_name,y0,t_span,step,*args):
    """
    fun_name: the name of the ODE to be solved like"fun_name(y0,t)"

    y0: ndarray, the initial value of the function at t=t_span[0]. and suggested shape of the y0 is the first dimension is the different particles, the second is different properties.

    t-span: the time span of the ODE to be solved like"[t_start, t_stop]"
    
    step: the step length of the t_span
    """

    ti=t_span[0]
    te=t_span[1]
    y=[]
    shape= y0.shape
    
    if len(shape)==1:
        n=1
        while ti<=te:
            y1=y0+fun_name(y0,ti,*args)*step
            if abs(y1.min()/y0.min())/step>100:
                print('warning: in the step ',[ti,ti+step],'too steep!! maybe you need a smaller step.')
            n+=1
            y0=y1
            
            ti=ti+step
            y.append(y0)
        if n<=10:
            print('maybe your step is too large!')

    else:
        n=1
        y0i=y0  #in theory y0i should be a list with several properties of one particle
        while ti<=te:
            y1i=y0+fun_name(y0i,ti,*args)*step
            if abs(y1i.min()/y0i.min())/step>100:
                print('warning: in the step ',[ti,ti+step],'too steep!! maybe you need a smaller step.')
            n+=1
            y0i=y1i
            ti= ti+step
            y.append(y0i)
        if n<=10:
            print('maybe your step is too large!')

    y=np.array(y)    

        
    return y


def ode(fun_name,y0,t_span,step,method='RK5',*args):
    """
    method: string. can be 'Euler', 'RK5' or 'Heun', the default method is 'RK5'
    """
    if method=='RK5':
        y=RK5(fun_name,y0,t_span,step,*args)

    if method=='Euler':
        y=Euler(fun_name,y0,t_span,step,*args)

    ## CWO: implement Heun
    # if method=='Heun':
    #     y=Heun(fun_name,y0,t_span,step)

    ## CWO: implement scipy.odeint method
    #if method=='odeint':
        #implement scipy.integrate.odeint..
    return y

