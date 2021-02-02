# Problem-1 : Plotting of user defined signal
#Importing required modules
import numpy as np
import matplotlib.pyplot as plt


#Inputs for discrete signal
T = input('Which type of signal would you like to enter?(Complex(c) or Real(r))')#Signal Type
n = input('Number of data points of the signal : ',) #Number of Data points 

#Cases for real and complex signal
if T == 'r' :                      #Real signal
    dat = np.zeros(int(n))         #Data of the signal
    for i in range(int(n)):        #User defining the signal
        dat[i] = input('Enter the ' + str(i+1) + 'th data point : ')#Inputting the signal 
    print(dat) #Printing the acquired data
    #Plot
    plt.stem(dat,use_line_collection=True,bottom = 0)#Plotting the data using stem
    plt.xlabel('n')                 # X-axis label
    plt.ylabel('Signal Value(X[n])')# Y-axis label
    plt.title('Signal X[n]')        #Title for the plot
else:                               #Complex signal
    dat = np.zeros((int(n),2))      #Data of the signal
    for i in range(int(n)):         #Enetring the data of the signal
        dat[i,0] = int(input('Enter the real part of '+ str(i+1) + 'th data point : ')) #Real part
        dat[i,1] = int(input('Enter the imaginary part of '+ str(i+1) + 'th data point : '))#Imaginary part
    print(dat)                      #Printing the data
    mag = np.zeros(int(n))          #Magnitude of the signal
    phi = np.zeros(int(n))          #Phase of the signal
    for i in range(int(n)):
        mag[i] = np.sqrt((dat[i,0]**2)+(dat[i,1]**2))             #Calculating the magnitude
        phi[i] = np.angle(complex((dat[i,0]),(dat[i,1])),deg=True)#Calculating the phase
    print(mag)                      #Printing Magnitude
    print(phi)                      #Printing phase
    #Plot
    plt.stem(mag,use_line_collection=True) #Plotting magnitude using stem
    plt.xlabel('n')                        #X-label
    plt.ylabel('Magnitude(|X[n]|)')        #Y-label
    plt.title('Magnitude of Complex Signal X[n]')#Title
    plt.show()                             #Plot
    plt.stem(phi,use_line_collection=True) #Plotting phase
    plt.xlabel('n')                        #X-label
    plt.ylabel('Phase in degrees')         #Y-label
    plt.title('Phase of Complex Signal X[n]')#Title
    plt.show()                             #plot

