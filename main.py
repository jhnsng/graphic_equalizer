import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile
from filtering import BandpassFilter

# parameters
order = 1   # filter order
fl = 20     # low passband freq
fh = 20000  # high passband freq

# Load the .wav file
sample_rate, audio_samples = wavfile.read('snippet_mono.wav')

# play the original audio file
sd.play(audio_samples, sample_rate, blocking=True)

# instantiate filter class
bandpass_filter = BandpassFilter()

# take fourier transform for audio spectrum
spectrum = np.abs(np.fft.fft(audio_samples))

# Normalize audio data -- this is what makes the filtered audio playback clear and not distorted
audio_samples = audio_samples.astype(float) # we need to change audio_samples (integers) to type float for the next line of code to work
audio_samples /= np.max(np.abs(audio_samples))

# apply filtering
butter = bandpass_filter.iir_filter(order, fl, fh, sample_rate)
sigout = bandpass_filter.filter(butter, audio_samples)
[zeros, poles, gain] = bandpass_filter.zpk(butter)

# play the filtered version
sd.play(sigout, sample_rate, blocking=True)

# plot spectrum
plt.plot(spectrum)
plt.show()


