#Problem-4 : DTFT symmetry properties
#importing required modules
import numpy as np
import matplotlib.pyplot as plt
#Function for calculating DTFT
def DTFT(data,w,n):              # data is the numpy array of signal, w is frequency,n is the sequence scale.
    N = len(w)                   # Number of points for w.
    DTFT = np.zeros(N)+np.ones(N)*1j          #Initializing DTFT
    for i in range(N):                        #computing DTFT
        dtft = 0
        for k in range(len(data)):
            dtft += data[k]*(np.cos(w[i]*n[k])+(np.sin(w[i]*n[k])*1j)) 
        DTFT[i]=dtft
    #MagnitudeSpectrum and Phase spectrum
    dtft_mag = [] #Magnitude Array
    dtft_phi = [] #Phase Array
    for i in range(N):#Calculating phase and magnitude
        dtft_mag+=[abs(DTFT[i])]#Magnitude = root(real^2 + img^2)
        dtft_phi+=[np.angle(DTFT[i],deg=True)]#Phase=arctan(img/real)
    #Real values Plot
    f1 = plt.figure(1) 
    plt.plot(w,DTFT.real)
    plt.xlabel('w')
    plt.ylabel('Real(X(e^jw))')
    plt.title('Real values')
    #Imaginary values Plot
    f2 = plt.figure(2) 
    plt.plot(w,DTFT.imag)
    plt.xlabel('w')
    plt.ylabel('Imag(X(e^jw))')
    plt.title('Imaginary')
    #Magnitude plot
    f3 = plt.figure(3) 
    plt.plot(w,dtft_mag)
    plt.xlabel('w')
    plt.ylabel('|X(e^jw)|')
    plt.title('Magnitude Spectrum')
    #Phase Plot
    f4= plt.figure(4)
    plt.plot(w,dtft_phi)
    plt.xlabel('w')
    plt.ylabel('Phase(X(e^jw))')
    plt.title('Phase Spectrum')
    plt.show()
    return(DTFT,dtft_mag,dtft_phi)
#4-a : The DTFT is conjugate symmetric for real signals.(X[e^jw]=X*[e^-jw])
#Example for verification - x : cosine
n = np.linspace(-5,5,11)   # n is the sequence points
N=10                       #periodicity
x = np.cos((2*np.pi/N)*n)  #signal
print("(a):The DTFT is conjugate symmetric for real signals.")
f5= plt.figure(5)
plt.stem(n,x,use_line_collection=True)#Ploting the delta
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Input signal')
plt.show()
w_0 = np.linspace(-np.pi,np.pi,100) # w_0 is frequency
a,b,c = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
d,e,f = np.conj(DTFT(x,-w_0,n))  #X*(e^-jw) of input signal
#statement to check if the given property is true
if (a==d).all():
    print("The property(a) is true")
else :
    print("The property(a) is false")
    
#4-b : The DTFT of a real and even signal is real and even.(X[e^jw]=X[e^-jw] if x[n]=x[-n])
#Example for verification - x : 2delta(n-1)+delta(n)+2delta(n+1) 
n = np.linspace(-6,6,num=13) # n is the sequence points
N = 5 # periodicity
x = np.zeros(13)#Delta Function
# delta[0]=1
x[5]=2
x[6]=1
x[7]=2
print("b:The DTFT of a real and even signal is real and even")
f6= plt.figure(6)
plt.stem(n,x,use_line_collection=True)#Ploting the delta
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Input signal')
plt.show()
w_0 = np.linspace(-np.pi,np.pi,100)  # w_0 is frequency
m,h,p = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
l,f,r = DTFT(x,-w_0,n)  #X*(e^-jw) of input signal.
#statement to check if the given property is true
if (m==l).all() and (m.imag==np.zeros(len(m))).all():#checking if imaginary part is 0 and if it is even.
    print("The property(b) is true")
else :
    print("The property(b) is false")  

#4-c : The DTFT of a real and odd signal is imaginary and odd.(X[e^jw]=-X[e^-jw] if x[n]=-x[-n])
#Example for verification - x : 2delta(n-1)-2delta(n+1)
n = np.linspace(-6,6,num=13)    # n is the sequence points
N = 5 # periodicity
x = np.zeros(13)#Delta Function
# dleta[0]=0
x[5]=-2
x[6]=0
x[7]=2
print("c:The DTFT of a real and odd signal is imaginary and odd.")
f6= plt.figure(6)
plt.stem(n,x,use_line_collection=True)#Ploting the delta
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Input signal')
plt.show()
w_0 = np.linspace(-np.pi,np.pi,100)    # w_0 is frequency
m,h,p = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
l,f,r = DTFT(x,-w_0,n)  #X(e^-jw) of input signal.
#statement to check if the given property is true
if (m==-l).all() and (m.real==np.zeros(len(m))).all(): #checking if real part is 0 and if it is odd.
    print("The property(c) is true")
else :
    print("The property(c) is false")
    
#4-d : The DTFT is conjugate anti symmetric for purely imaginary signals.(X[e^jw]=-X[e^-jw]=X*[e^-jw] if x[n] is purely imaginary)
#Example for verification - x : jdelta(n)
n = np.linspace(-6,6,num=13)          # n is the sequence points
N = 5 # periodicity
x = np.zeros(13)+(np.ones(13)*1j)#Delta Function
for i in range(len(n)):
    if i==6:
        x[i]=1*1j
    else:
        x[i]=0

print("d:The DTFT is conjugate anti symmetric for purely imaginary signals.")
w_0 = np.linspace(-np.pi,np.pi,100)      # w_0 is frequency
m,h,p = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
#l,f,r = DTFT(x,-w_0,n)  #X(e^-jw) of input signal.
p,q,s = np.conj(DTFT(x,-w_0,n))
#statement to check if the given property is true
if  (m==-p).all(): # checking if it is conjugate anti symmetric.
    print("The property(d) is true")
else :
    print("The property(d) is false") 
    
#4-e : The DTFT of an imaginary and even signal is imaginary and even.(X[e^jw]=X[e^-jw] if x[n] is  imaginary and even )
#Example for verification - x : jdelta(n-1)+ jdelta(n+1)
n = np.linspace(-6,6,num=13)           # n is the sequence points
N = 5 # periodicity
x = np.zeros(13)+(np.ones(13)*1j)#Delta Function
for i in range(len(n)):
    if i==5 or i==7:
        x[i]=1+(1*1j)
    else:
        x[i]=0

print("e:The DTFT of an imaginary and even signal is imaginary and even.")
w_0 = np.linspace(-np.pi,np.pi,100)    # w_0 is frequency
m,h,p = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
l,f,r = DTFT(x,-w_0,n)  #X(e^-jw) of input signal.

#statement to check if the given property is true
if  (m==l).all() and not (m.imag == np.zeros(len(m))).all(): #checking if imaginary part is not 0 for some and if it is even.
    print("The property(e) is true")
else :
    print("The property(e) is false") 
    
#4-f : The DTFT of an imaginary and odd signal is real and odd.(X[e^jw]=-X[e^-jw] if x[n] is  imaginary and odd )
#Example for verification - x : jdelta(n-1)- jdelta(n+1)
n = np.linspace(-6,6,num=13)      # n is the sequence points
N = 5 # periodicity
x = np.zeros(13)+(np.ones(13)*1j)#Delta Function
for i in range(len(n)):
    if i==5:
        x[i]=(-(1*1j))
    elif i==7:
        x[i]=(1*1j)
    else:
        x[i]=0+(0*1j)

print("f :The DTFT of an imaginary and odd signal is real and odd.")
w_0 = np.linspace(-np.pi,np.pi,100)           # w_0 is frequency
m,h,p = DTFT(x,w_0,n)  #DTFT of input signal X(e^jw)
l,f,r = DTFT(x,-w_0,n)  #X(e^-jw) of input signal.

#statement to check if the given property is true
if  (m==-l).all() and  (m.imag == np.zeros(len(m))).all(): #checking if imaginary part is 0 and if it is odd.
    print("The property(f) is true")
else :
    print("The property(f) is false") 
    
    
    

