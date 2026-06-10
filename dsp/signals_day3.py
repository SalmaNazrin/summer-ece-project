import scipy
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt
f1=5
f2=50
f_cutoff=20
f_sampling=1000
t=np.linspace(0,1,f_sampling)
sig=np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)
fig, ax = plt.subplots(5, 1, figsize=(8,8))
ax[0].plot(t, sig)
np.random.seed(42)
noise=np.random.normal(0,0.5,size=t.shape)
ax[0].set_title("clean signal")
ax[1].set_title("noise")
ax[2].set_title("noisy signal")
ax[3].set_title("lpf")
ax[4].set_title("hpf")
ax[1].plot(t,noise)
noisy_sig=noise+sig
ax[2].plot(t,noisy_sig)

def lowpassfilter( input_signal,cutoff,order,sampling):
    nyq=sampling/2
    normalized_cutoff=cutoff/nyq
    b,a=butter(order, normalized_cutoff, btype="low")
    return filtfilt(b,a,input_signal)
filtered=lowpassfilter(noisy_sig,f_cutoff,4,f_sampling )
ax[3].plot(t,filtered)
def highpassfilter( input_signal,cutoff,order,sampling):
    nyq=sampling/2
    normalized_cutoff=cutoff/nyq
    b,a=butter(order, normalized_cutoff, btype="high")
    return filtfilt(b,a,input_signal)
highfiltered=highpassfilter(noisy_sig,f_cutoff,4,f_sampling)
ax[4].plot(t,highfiltered)
plt.tight_layout()
plt.show()
 