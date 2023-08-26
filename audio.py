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
        # We need to change audio_samples (integers) to type float for the next line of code to
        self.original_samples = self.original_samples.astype(float)
        self.original_samples /= np.max(np.abs(self.original_samples))

    def play_original_audio(self):
        sd.play(self.original_samples, self.sample_rate, blocking=True)


    # Multiplies each frequency band by the gain from slider_values
    # Sums the resulting scaled frequency bands
    # Returns the full filtered samples array with proper gain adjustments
    def adjust_freqband_gain(self, filtered_bands, slider_values):
        
        self.scaled_samples = [0]*len(self.original_samples)
        for band, gain in zip(filtered_bands, slider_values):
            linear_gain = 10 ** (gain / 20)
            self.scaled_samples += band*linear_gain
        
        return self.scaled_samples

    # Apply bandpass filter to each center frequency 
    # freqs is the array of center frequencies
    # Returns filtered samples array with adjusted gain for each band of frequencies
    def filter_center_freqs(self, order, freqs, slider_values):
        
        # instantiate bandpass filter
        bandpass_filter = BandpassFilter()
        
        self.__butter = [0]*len(freqs)
        self.filtered_samples_array = [0]*len(freqs)

        for i in range(0, len(freqs)):
            # center freq +/- bw to get cutoff freq -- adjustable
            bw = (freqs[i])/3
            # get low/high cut off freqs from center freq
            fl = freqs[i] - bw 
            fh = freqs[i] + bw

            self.__butter[i] = bandpass_filter.iir_filter(order, fl, fh, self.sample_rate) # __butter automatically becomes a 2D array
            self.filtered_samples_array[i] = bandpass_filter.filter(
                 self.__butter[i], self.original_samples) # the same original samples are used for each iteration
            
        # Apply the proper gain for each center frequency according to slider values
        return self.adjust_freqband_gain(self.filtered_samples_array, slider_values)

    def play_filtered_audio(self, order, freqs, slider_values):

        self.scaled_sampless = self.filter_center_freqs(order, freqs, slider_values)
        sd.play(self.scaled_sampless, self.sample_rate, blocking=True)

        '''
        # instantiate bandpass filter
        bandpass_filter = BandpassFilter()

        self.__butter = bandpass_filter.iir_filter(
            order, fl, fh, self.sample_rate)
        self.filtered_samples = bandpass_filter.filter(
            self.__butter, self.original_samples)
        sd.play(self.filtered_samples, self.sample_rate, blocking=True)

        '''