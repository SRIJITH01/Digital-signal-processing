#Problem-3 : Computing DTFT of given input signal
#Importing the required modules
import numpy as np
import matplotlib.pyplot as plt

#Inputs for discrete signal
T = input('Which type of signal would you like to enter?(Complex(c) or Real(r))')#Signal Type
n = input('Number of data points of the signal : ',) #Number of Data points 
N = 100  #Number of samples of w
w = np.linspace(-np.pi,np.pi,N)#Frequency
#Cases for real and complex signal
if T == 'r' :                      #Real signal
    dat = np.zeros(int(n))         #Data of the signal
    for i in range(int(n)):        #User defining the signal
        dat[i] = input('Enter the ' + str(i+1) + 'th data point : ')#Inputting the signal 
    print(dat) #Printing the acquired data
        #Plot of entered signal
    f1 = plt.figure(1)
    plt.stem(dat,use_line_collection=True,bottom = 0)#Plotting the data using stem
    plt.xlabel('n')                 # X-axis label
    plt.ylabel('Signal Value(X[n])')# Y-axis label
    plt.title('Signal X[n]')        #Title for the plot
    #DTFT
    DTFT = np.zeros(N)+np.ones(N)*1j #Initializing DTFT
    for i in range(N):               #computing DTFT
        dtft = 0
        for k in range(int(n)):
            dtft += dat[k]*(np.cos(w[i]*k)+(np.sin(w[i]*k)*1j)) 
        DTFT[i]=dtft
    #MagnitudeSpectrum and Phase spectrum
    dtft_mag = []                          #Magnitude Array
    dtft_phi = []                          #Phase Array
    for i in range(N):                     #Calculating phase and magnitude
        dtft_mag+=[abs(DTFT[i])]           #Magnitude = root(real^2 + img^2)
        dtft_phi+=[np.angle(DTFT[i],deg=True)]#Phase=arctan(img/real)
    #Magnitude Plot
    f2 = plt.figure(2) 
    plt.plot(w,dtft_mag)
    plt.xlabel('w')
    plt.ylabel('|X(e^jw)|')
    plt.title('Magnitude Spectrum')
    #Phase Plot
    f3= plt.figure(3)
    plt.plot(w,dtft_phi)
    plt.xlabel('w')
    plt.ylabel('Phase(X(e^jw))')
    plt.title('Phase Spectrum')
    plt.show()

        
else:                               #Complex signal
    data = np.zeros(int(n))+np.ones(int(n))*1j
    dat = np.zeros((int(n),2))      #Data of the signal
    for i in range(int(n)):         #Enetring the data of the signal
        dat[i,0] = int(input('Enter the real part of '+ str(i+1) + 'th data point : ')) #Real part
        dat[i,1] = int(input('Enter the imaginary part of '+ str(i+1) + 'th data point : '))#Imaginary part
        data[i] = dat[i,0]+(dat[i,1]*1j)#The data of the complex signal
    print(dat)                      #Printing the data
    mag = np.zeros(int(n))          #Magnitude of the signal
    phi = np.zeros(int(n))          #Phase of the signal
    for i in range(int(n)):
        mag[i] = np.sqrt((dat[i,0]**2)+(dat[i,1]**2))             #Calculating the magnitude
        phi[i] = np.angle(complex((dat[i,0]),(dat[i,1])),deg=True)#Calculating the phase
    print(mag)                      #Printing Magnitude
    print(phi)                      #Printing phase
    #Plot of entered signal
    f1 = plt.figure(1)
    plt.stem(mag,use_line_collection=True) #Plotting magnitude using stem
    plt.xlabel('n')                        #X-label
    plt.ylabel('Magnitude(|X[n]|)')        #Y-label
    plt.title('Magnitude of Complex Signal X[n]')#Title
    f2 = plt.figure(2)
    plt.stem(phi,use_line_collection=True) #Plotting phase
    plt.xlabel('n')                        #X-label
    plt.ylabel('Phase in degrees')         #Y-label
    plt.title('Phase of Complex Signal X[n]')#Title
    #DTFT
    DTFT = np.zeros(N)+np.ones(N)*1j
    for i in range(N):
        dtft = 0                                                  #Initializing DTFT
        for k in range(int(n)):                                   #computing DTFT
            dtft += data[k]*(np.cos(w[i]*k)+(np.sin(w[i]*k)*1j)) 
        DTFT[i]=dtft
    #MagnitudeSpectrum and Phase spectrum
    dtft_mag = [] #Magnitude Array
    dtft_phi = [] #Phase Array
    for i in range(N):#Calculating phase and magnitude
        dtft_mag+=[abs(DTFT[i])]#Magnitude = root(real^2 + img^2)
        dtft_phi+=[np.angle(DTFT[i],deg=True)]#Phase=arctan(img/real)
    #Magnitude Plot
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
    
