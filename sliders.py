import tkinter as tk
from tkinter import ttk

# the frequency bands used in the GEQ
frequencies = [
    31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000, 16000
]

# GUI window
window = tk.Tk()
window.title('Graphic Equalizer')

# Create a frame to hold the sliders
slider_frame = ttk.Frame(window)
slider_frame.pack()

# Create sliders for each frequency
sliders = []
for freq in frequencies:
    scale = tk.Scale(slider_frame, from_=6, to=-6,
                     orient=tk.VERTICAL, label=f'{freq}Hz')
    scale.pack(side=tk.LEFT, padx=5, pady=5)
    sliders.append(scale)

# Run the GUI loop
window.mainloop()
