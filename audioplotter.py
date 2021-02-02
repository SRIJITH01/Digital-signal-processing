#Problem-5 Wave files signals
#importing required modules
import numpy as np
import matplotlib.pyplot as plt
import wave 

#Function for calculating DTFT
def DTFT(data,w):# data is the numpy array of audio signal and w is frequency
    N = len(w) # Number of points for w.
    DTFT = np.zeros(N)+np.ones(N)*1j# Initializing DTFT
    for i in range(N):  # calculating DTFT
        dtft = 0
        for k in range(len(data)):
            dtft += data[k]*(np.cos(w[i]*k)+(np.sin(w[i]*k)*1j)) 
        DTFT[i]=dtft
        
    #MagnitudeSpectrum and Phase spectrum
    dtft_mag = [] #Magnitude Array
    dtft_phi = [] #Phase Array
    for i in range(N):#Calculating phase and magnitude
        dtft_mag+=[abs(DTFT[i])]#Magnitude = root(real^2 + img^2)
        dtft_phi+=[np.angle(DTFT[i],deg=True)]#Phase=arctan(img/real)
    
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

#Function for plotting the audio signal
def Audio_plotter(sound_file):#soundfile is the required audio file name
    sound = wave.open(sound_file, "r") # reading the sound file
    # Extract Raw Audio from Wav File
    signal = sound.readframes(-1)  #Reading the all the frames of audio signal into bytes
    s = np.frombuffer(signal,dtype=np.uint8) # converting bytes to nparray
    f_rate = sound.getframerate() # finding the framerate of the audio signal
    t = np.linspace(0,len(signal)/f_rate,num=len(signal)) #calculating timescale of the audio signal
    # Plotting the audio signal in time domain
    f1 = plt.figure(1) 
    plt.plot(t,s)
    plt.xlabel('t') #labeling time
    plt.ylabel('X[t]') 
    plt.title('Audio signal') 
    w_0 = np.linspace(-np.pi,np.pi,num=100) #frequency for DTFT
    print("For  " + str(sound_file))
    a,b,c = DTFT(s,w_0) #Using DTFT function

Audio_plotter("armageddon.wav") # Plotter for armageddon file
Audio_plotter("alarm.wav") # Plotter for alarm file
Audio_plotter("cry.wav") # Plotter for cry file
Audio_plotter("wow.wav") #Plotter for wow file


#Comments
#1-For armageddon.wav file the magnitude spectrum is even,concentrated around low frequencies 
#  and phase spectrum is odd.
#2-For alarm.wav file audio signal lookslike a periodic signal, the magnitude spectrum is even,has major spike 
# at 0,smaller spikes at higher frequencies and phase spectrum is odd.
#3-For cry.wav file  the magnitude spectrum is even,has major spikes at -0.5,+0.5.very small spikes 
# at other frequencies and phase spectrum is odd.
#4-For wow.wav file , audio signal is concentrated around mid duration the magnitude spectrum is even,
#has major spikes at many frequencies and phase spectrum is odd.
