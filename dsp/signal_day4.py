import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy.signal import butter, filtfilt
data,samplerate=sf.read("dspnew.wav")
fig,ax=plt.subplots(4,1,figsize=(10,10))
ax[0].set_title("real audio signal")
ax[0].plot(data)

fftresult=np.fft.fft(data)
fftfreq=np.fft.fftfreq(len(data),d=1/samplerate)
fftmag=np.abs(fftresult)
positive=fftfreq>=0
cleanfreq=fftfreq[positive]
cleanmag=fftmag[positive]
ax[1].set_title("fft")
ax[1].plot(cleanfreq,cleanmag)

def lpf(data ,order, sampling, cutoff):
    normalized_cutoff=2*cutoff/sampling
    b,a=butter(order, normalized_cutoff, btype="low")
    return filtfilt(b,a,data)
lpfresult=lpf(data,4,samplerate,3000)
ax[2].set_title("lpf")
ax[2].plot(lpfresult)

def hpf(data ,order, sampling, cutoff):
    normalized_cutoff=2*cutoff/sampling
    b,a=butter(order, normalized_cutoff, btype="high")
    return filtfilt(b,a,data)
hpfresult=hpf(data,4,samplerate,300)
ax[3].set_title("hpf")
ax[3].plot(hpfresult)
plt.show()
