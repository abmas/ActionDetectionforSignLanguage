import numpy as np
from scipy.io.wavfile import write

# Parameters for the beep
fs = 44100            # Sample rate (Hz)
duration = 0.1        # Duration in seconds (100 ms)
frequency = 440       # Frequency in Hz (A4 note)

# Generate time samples
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Create the sine wave with amplitude 0.5 (to avoid clipping)
amplitude = 0.5
audio = amplitude * np.sin(2 * np.pi * frequency * t)

# Apply a fade-out envelope for smoothness
fade = np.linspace(1, 0, audio.shape[0])
audio = audio * fade

# Convert to 16-bit PCM format
audio_int16 = np.int16(audio * 32767)

# Write to a WAV file
write("beep.wav", fs, audio_int16)

print("beep.wav has been created.")
