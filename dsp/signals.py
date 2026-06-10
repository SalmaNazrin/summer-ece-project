import numpy as np 
import matplotlib.pyplot as plt


# sine wave with frequency 5
x=np.linspace(0,1,1000)
y1=np.sin(x * 2* np.pi *5)
plt.title("wave 5hz")
plt.xlabel("time", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(x, y1)
plt.show()
plt.close()
#sine wave with frequency 50
y2=np.sin(x*2*np.pi*50)
plt.title("wave 50 hz")
plt.xlabel("time", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(x,y2)
plt.show()
plt.close()

#sine wave mixed 
sinemix=y1+y2
plt.title("clean mixed wave")
plt.xlabel("time", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(x,sinemix)
plt.show()
plt.close()

#noice in sound wave
np.random.seed(42)
noise = np.random.uniform(0, 0.5, size=x.shape) #x.shape means x has 1000 values as assigned . so we can replace size=x.shape with 1000. 
#this creates 1000 values between 0 and 0.5 and randomly assigns a value for noise
noisy = sinemix + noise
plt.title("noise")
plt.xlabel("time", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(x, noise) # NOISE y value ranges from 0 to 0.5 since random mix is ranged accordingly in line 34
plt.show()
plt.close()

plt.title("noisy signal")
plt.xlabel("time", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(x, noisy)   
plt.show()
plt.close()

N = len(x)
fft_vals = np.fft.fft(noisy)
fft_mag = np.abs(fft_vals) / N  
freqs = np.fft.fftfreq(N, d=x[1] - x[0])
 
pos_mask = freqs >= 0
freqs_pos = freqs[pos_mask]
fft_pos = fft_mag[pos_mask]
plt.title("fft")
plt.xlabel("frequency", fontsize=12, color="black")
plt.ylabel("fourier tranformed", fontsize=12, color="black")
plt.plot(freqs_pos, fft_pos, color='mediumorchid', linewidth=1.2)
plt.show()
plt.close()


