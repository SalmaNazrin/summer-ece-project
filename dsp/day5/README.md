Loaded three audio signals — a voice recording, a sustained vowel 'A', and a whistle — and visualised each as a spectrogram using Matplotlib's built-in specgram function. Unlike FFT which shows average frequency
content over the entire signal, a spectrogram reveals how frequency content changes over time by applying FFT across sliding windows.

Voice recording: Energy is concentrated in the lower frequencies (0–5000Hz) with bright vertical streaks corresponding to spoken words and dark gaps representing silence. 
Higher frequencies carry significantly less energy.

Vowel 'A': Shows clear horizontal bands at evenly spaced frequencies — the fundamental frequency and its harmonics. 
This ladder pattern is the acoustic signature of a sustained vowel and is the basis of how speech recognition systems identify vowel sounds.

Whistle: Shows curved lines rising diagonally from bottom-left to top-right,revealing pitch increasing over time. 
The parallel lines above the fundamental are harmonics rising in step. This time-varying frequency structure is invisible in a plain FFT plot — the spectrogram's key advantage.

Concepts covered: spectrogram, time-frequency analysis, harmonics, fundamental frequency, sliding window FFT, pitch variation

Libraries used: Matplotlib, SoundFile
