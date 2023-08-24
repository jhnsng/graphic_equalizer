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


######EVERYTHING BELOW THIS IS CHATGPT##################

# Define callback function for audio streaming


def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    spectrum = np.fft.fft(indata)
    # Display only positive frequencies
    line.set_ydata(np.abs(spectrum[:chunk_size//2]))
    fig.canvas.draw()
    fig.canvas.flush_events()


# Set up real-time audio streaming
chunk_size = 1024
stream = sd.InputStream(callback=audio_callback,
                        channels=1, samplerate=sample_rate)

# Create a real-time spectrum visualization
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
frequencies = np.fft.fftfreq(chunk_size, 1 / sample_rate)
line, = ax.plot(frequencies[:chunk_size//2],
                np.zeros(chunk_size//2))  # Initial plot
ax.set_xlim(0, sample_rate / 2)
ax.set_ylim(0, 200)  # Adjust the y-axis limit as needed

# Start the audio stream
stream.start()

# Wait for user to close the plot
plt.ioff()
plt.show()

# Stop the audio stream
stream.stop()
