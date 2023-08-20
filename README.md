# graphic_equalizer

This is the repository for an audio graphic equalizer implemented in Python. This project employs knowledge in OOP and signal processing.

This project was inspired by an 8-year-old Reddit comment:

"Here's a good project that's all code and pure DSP (not a lot of book keeping code to do).

What you could make is something called a graphic equalizer. You find these devices in music players and mixing consoles at music venues. What it does is change the frequency response of an audio signal in order to compensate for speakers and room effects. Think high-low-mid boost/cut on a stereo, but with more control.

A graphic EQ looks like a bunch of sliders, each marked with a frequency. Moving the slider up boosts the gain of that frequency, moving it down cuts it. You have a bunch of sliders equally spaced across the spectrum from 20Hz to 20,000Hz (audible range), so moving the sliders is a graphic way of adjusting the audible frequency response (hence the name).

The way a graphic EQ (GEQ as it's notated sometimes) works is by putting a bunch of bandpass filters in parallel. On commercial systems you might get 8 bands, in professional you would see 64 or so. Each bandpass filter has a fixed center frequency, and the slider controls the gain of an amplifier. The outputs of every amplifier is summed together at the output. There is some nuance to it, mostly that the Q factor of the filters must be selected such that when all the amplifier's gains are 1, the sum of the filters' magnitude responses is 1. This depends on the number of filter bands. I recommend an IIR filter approach, that way you just need to adjust Q factor and not the transition band and you only need 4 filter taps."
