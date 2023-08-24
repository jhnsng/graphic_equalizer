from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from filtering import BandpassFilter


class Audio():

    def __init__(self):
        pass

    def read_file(self, file_to_read):
        self.file_to_read = file_to_read
        # Load the .wav file
        self.sample_rate, self.original_samples = wavfile.read(
            self.file_to_read)
        return self.sample_rate, self.original_samples

    def write_file(self, file_to_write, filtered_samples):
        self.file_to_write = file_to_write
        self.filtered_samples = filtered_samples
        # Write to .wav file
        wavfile.write(self.file_name, self.sample_rate, self.filtered_samples)

    def normalize_samples(self):
        # Normalize audio data -- this is what makes the filtered audio playback clear and not distorted
        # we need to change audio_samples (integers) to type float for the next line of code to
        self.original_samples = self.original_samples.astype(float)
        self.original_samples /= np.max(np.abs(self.original_samples))

    def play_original_audio(self):
        sd.play(self.original_samples, self.sample_rate, blocking=True)

    def play_filtered_audio(self, fl, fh, order):

        # instantiate bandpass filter
        bandpass_filter = BandpassFilter()

        self.__butter = bandpass_filter.iir_filter(
            order, fl, fh, self.sample_rate)
        self.filtered_samples = bandpass_filter.filter(
            self.__butter, self.original_samples)
        sd.play(self.filtered_samples, self.sample_rate, blocking=True)
