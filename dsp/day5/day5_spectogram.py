import soundfile as sf
input_sig,sample1=sf.read("dspnew.wav")
whistle,sample2=sf.read("whistle.wav")
vowel,sample3=sf.read("vowel_a.wav")
import matplotlib.pyplot as plt
def spectogram(data,fs):
 if data.ndim == 2:        # if stereo, take left channel only some audios may have 2 directions. spectrogram only takes monochannel
         data = data[:, 0]
 plt.specgram (data,Fs=fs, cmap='inferno') #dont forget to put Fs= here
 plt.colorbar(label="Intensity in dB")
 plt.title("spectrogram")
 plt.show()
 plt.close()
spectogram(input_sig,sample1)
spectogram(whistle,sample2)
spectogram(vowel,sample3)

