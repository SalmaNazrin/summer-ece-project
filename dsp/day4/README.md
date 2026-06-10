Loaded a real voice recording and applied FFT to analyse its frequency content. Observed that human voice energy is concentrated in the 0–1000Hz range. Built reusable lpf() and hpf() filter functions and applied them to the voice signal, visualising the raw waveform, frequency spectrum, low-pass filtered output, and high-pass filtered output in a single 4-subplot figure.
Concepts covered: real-world signal loading, voice frequency characteristics, harmonics, reusable filter functions, multi-plot visualisation
Libraries used: NumPy, SciPy, Matplotlib, SoundFile
