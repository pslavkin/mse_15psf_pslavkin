import numpy as np
import scipy.signal as sc
import simpleaudio as sa

f         = 200
fs        = 44100 
sec       = 10

t    = np.arange(0,sec,1/fs)
note = (2**15-1)*np.sin(2 * np.pi * f * t)
#note = (2**15-1)*sc.sawtooth(2 * np.pi * f * t)
#note = (2**15-1)*sc.square(2 * np.pi * f * t)

audio = note.astype(np.int16)
for i in range(100):
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

