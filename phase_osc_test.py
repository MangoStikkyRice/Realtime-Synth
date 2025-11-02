import numpy as np
import matplotlib.pyplot as plt

# Pi
PI = np.pi

# Oscillator class
class Oscillator:
    def __init__(self, sample_rate, frequency, amplitude=1, initial_phase=0):
        
        # User parameters
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = initial_phase
        
    def process(self, duration, target_frequency = None):
        
        # No glide if target frequency not specified
        if target_frequency is None:
            target_frequency = self.frequency

        # Calculate number of samples to process
        num_samples = int(self.sample_rate * duration)
        
        # Create a linearly spaced buffer accounting for
        # the target frequency.
        frequency_steps = np.linspace(self.frequency, target_frequency, num_samples)
        increment = 2 * PI * frequency_steps / self.sample_rate
        
        # Calculate the current phase
        curr_phase = np.mod(self.phase + np.cumsum(increment), 2 * PI)
        
        # Update the internal storage for phase
        self.phase = curr_phase[-1]
        
        # Update the internal storage for frequency if needed
        self.frequency = target_frequency
        
        # Return a samples array
        return self.amplitude * np.sin(curr_phase)

osc_1 = Oscillator(sample_rate=48000, frequency=440)

# Plot
plt.figure(figsize=(10, 4))

# Plot the first 300 samples
plt.plot(osc_1.process(duration=0.002)[:300])
plt.title("Generated Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()