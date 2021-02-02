#Problem-2 : Plotting of various basic signals
#Importing required modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Delta Signal or Unit Impulse Signal 
n = np.linspace(-5,5,num=11) #Length of the signal being plot 
delta = np.zeros(11)         #Delta Functions data
delta[5]=1                   #delta[0]=1
print('Impulse Signal')      #Signal Name
#Plot
plt.stem(n,delta,use_line_collection=True)#Ploting the delta
plt.xlabel('n')       #X-label
plt.ylabel('Delta[n]')#Y-label
plt.title('Impulse Function')#Title
plt.show()


#Unit Step Signal
print('Unit Step Signal')
U = np.zeros(11)            #Step Functions data
for i in range(11):         #u[n]=1 when n>=0
    if(i>4):
        U[i]=1
#Plotting the unit step function
plt.stem(n,U,use_line_collection=True)#Ploting the step
plt.xlabel('n') #X-label
plt.ylabel('u[n]')#Y-label
plt.title('Unit Step Function')
plt.show()


#Real Exponential Signal
print('Real Exponential Signal')
a = float(input('Enter the parameter of exponential :'))# parameter for exponential funtion-a^n
e = np.zeros(20)                 #exponential functions data array
d = [i for i in range(20) ]      #Power
for i in range(20):              #Calculating exponential
    e[i] = a**d[i]
    #Plot
plt.stem(d,e,use_line_collection=True)
plt.xlabel('n')
plt.ylabel('e[n]')
plt.title('Real Exponential Signal')
plt.show()


#Real Sinusoidal signal-Asin(w[n]+phi)
print('Real Sinusoidal Signal')
A = float(input('Enter the amplitude of the sinusoidal :')) #Amplitude
f = float(input('Enter the frequency of the sinusoidal :'))#Frequency
w = 2*np.pi*f
phi = float(input('Enter the phase shift of the sinusoidal in degrees : '))#phase
phi = phi*(np.pi/180)
s = np.zeros(11)
for i in range(11): #Calculating the sin function
    s[i] = A*np.sin(w*n[i] + phi)
#Plot
plt.stem(n,s,use_line_collection=True)
plt.xlabel('n')
plt.ylabel('sin[2pif*n+phi]')
plt.title('Real Sinusoidal Signal')
plt.show()


#Complex Sinusoidal - e^(sigma+jw_0)n
print('Complex Sinusoidal Signal')
num = 300 #Number of Samples
sigma = float(input('Enter the value of sigma for the complex exponential :'))#Sigma
p = float(input('Enter the required periodicity of complex sinusoidal :'))#Periodicity 
w_0 = 2*np.pi/p
n = [i for i in range(num)] #Sequence
#x[n] = e^(sigma*n)(cos(w_0*n)+jsin(w_0*n)
x = [np.exp(sigma*i)*(np.cos(w_0*i)+(np.sin(w_0*i))*1j) for i in n ]#Calculating the data
real_x = [r.real for r in x] #Extracting the real part
img_x = [c.imag for c in x] #Extracting the imaginary part
#Plot
fig = plt.figure()   
ax = fig.gca(projection='3d')
ax.plot(n,real_x,img_x,label= 'Complex Sinusoidal')
ax.legend()
plt.show()
