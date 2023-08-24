"""
This code handles user requests and interactions with the GUI using tkinter button and slider widgets.
"""
import tkinter as tk
from tkinter import ttk
from audio import Audio

file_to_read = 'snippet_mono.wav'

# frequency bands in Hz (ISO standard 10-band GEQ)
frequencies = [
    31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000, 16000
]

# instantiate Audio class (Note: not to be confused with the module named "audio")
audio = Audio()

# read input wav file
[sample_rate, original_samples] = audio.read_file(file_to_read)

# parameters
order = 1   # filter order
fl = 6000   # low passband freq
fh = 20000  # high passband freq


class Interface(tk.Tk):
    """
    Class for the user interface that inherits from the tkinter Tk superclass.
    """

    def __init__(self):
        super().__init__()  # constructor for tkinter superclass
        self.initialize()

    def initialize(self):
        self.title('Graphic Equalizer')
        self.initialize_buttons()
        self.initialize_sliders()
        self.mainloop()    # the tkinter GUI main loop

    def on_button1_click(self):
        audio.play_original_audio()

    def on_button2_click(self):
        audio.normalize_samples()
        audio.play_filtered_audio(fl, fh, order)

    def initialize_buttons(self):
        button1_frame = ttk.Frame(self)
        button1_frame.pack()
        button2_frame = ttk.Frame(self)
        button2_frame.pack()

        play_original_button = tk.Button(
            button1_frame, text="Play Original", command=self.on_button1_click)
        play_filtered_button = tk.Button(
            button2_frame, text="Play Filtered", command=self.on_button2_click)

        play_original_button.pack()
        play_filtered_button.pack()

    def initialize_sliders(self):
        # Create a frame to hold the sliders
        slider_frame = ttk.Frame(self)
        slider_frame.pack()

        # Create sliders for each frequency
        sliders = []
        for freq in frequencies:
            scale = tk.Scale(slider_frame, from_=6, to=-6,
                             orient=tk.VERTICAL, label=f'{freq}Hz')
            scale.pack(side=tk.LEFT, padx=5, pady=5)
            sliders.append(scale)


interface = Interface()
