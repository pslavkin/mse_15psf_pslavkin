import numpy as np
import simpleaudio as sa

frequency = 2500# Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 10  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = (2**15-1)*np.sin(20+(frequency*t/max(t)) * t * 2 * np.pi)
#note = (2**15-1)*np.sin(frequency* t * 2 * np.pi)


# Ensure that highest value is in 16-bit range
#audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = note.astype(np.int16)

# Start playback
for i in range(100):
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    # Wait for playback to finish before exiting
    play_obj.wait_done()


