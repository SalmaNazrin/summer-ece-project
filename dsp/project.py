import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

CHUNK = 2048
RATE = 44100

# Store latest audio chunk
latest = np.zeros(CHUNK)

def callback(indata, frames, time, status):
    global latest
    latest = indata[:, 0].copy()

# Set up plot
fig, ax = plt.subplots(figsize=(10, 4))
freqs = np.fft.rfftfreq(CHUNK, 1/RATE)
line, = ax.plot(freqs, np.zeros(len(freqs)), color='cyan')
ax.set_xlim(0, 3000)
ax.set_ylim(0, 500)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlabel("Frequency (Hz)", color='white')
ax.set_ylabel("Amplitude", color='white')
ax.set_title("Live Microphone FFT — speak or whistle", color='white')
ax.tick_params(colors='white')

def update(frame):
    fft = np.abs(np.fft.rfft(latest))
    line.set_ydata(fft)
    return line,

# Start mic stream
stream = sd.InputStream(samplerate=RATE, blocksize=CHUNK,
                        channels=1, callback=callback)
stream.start()

ani = animation.FuncAnimation(fig, update, interval=50, blit=True)
plt.tight_layout()
plt.show()

stream.stop()