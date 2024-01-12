# code for initializing bandpass filter class

from scipy.signal import butter, sosfilt, sos2zpk, iirfilter


class BandpassFilter():

    def __init__(self):
        pass

    def butter_bandpass(self, order, f_l, f_h, f_s):
        self.order = order
        self.f_l = f_l
        self.f_h = f_h
        self.f_s = f_s
        return butter(self.order, [self.f_l, self.f_h], btype='band', analog=False, output='sos', fs=float(self.f_s))

    def iir_filter(self, order, f_l, f_h, f_s):
        self.order = order
        self.f_l = f_l
        self.f_h = f_h
        self.f_s = f_s
        return iirfilter(self.order, [self.f_l, self.f_h], btype='band', analog=False, output='sos', fs=self.f_s)

    def filter(self, sos, x):
        self.sos = sos # second order sections
        self.x = x
        output = sosfilt(self.sos, self.x)
        return output

    def zpk(self, sos):
        self.sos = sos
        return sos2zpk(sos)
