import numpy as np
from utility.logger import LoggerIfc

class NoiseGenerator:
    def __init__(self) -> None:
        self.log = LoggerIfc("Noise")
        self.log.info("Noise initialized.")

    def getNoise(self, duration : float = 1e-2, sample_rate : float = 1e3, severity : float = 1) -> np.ndarray:
        """
        Generate noise.

        Args:
            duration (float): The duration of the waveform in seconds.
            sample_rate (float): The sampling rate in samples per second.

        Returns:
            numpy.ndarray: The noise as a numpy array.

        """
        return np.random.randn(int(sample_rate * duration)) * severity