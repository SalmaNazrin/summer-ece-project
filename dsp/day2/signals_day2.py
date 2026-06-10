import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(0,1,1000)
sinemix=np.sin(2*np.pi* t*5)+np.sin(2*np.pi* t*50)
fs=1000
fftresult=np.fft.fft(sinemix)
fftfreq=np.fft.fftfreq(fs, d=t[1]-t[0])
fftmag=np.abs(fftresult)/fs
pos_mask = fftfreq>=0 #we are only taking positive values
freq_pos =fftfreq[pos_mask]
fft_pos = fftmag[pos_mask]
plt.title("fft")
plt.xlabel("freq", fontsize=12, color="black")
plt.ylabel("amplitude", fontsize=12, color="black")
plt.plot(freq_pos, fft_pos)
plt.xlim(0,100)
plt.show()
plt.close()