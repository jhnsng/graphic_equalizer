import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

sos = signal.iirfilter(2, [20, 20000], btype='band',
                       analog=False, fs=48000, output='sos')

w, h = signal.sosfreqz(sos, 48000, fs=48000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
plt.show()
