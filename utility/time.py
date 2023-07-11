import numpy as np
from time import perf_counter

class Time:
    """
    A class for generating time axis and plotting waveforms.
    """
    @staticmethod
    def getTimeAxis(duration : float = 1e-2, sample_rate : float = 1e3) -> np.ndarray:
        """
        Generate the time axis for a given duration.

        Args:
            duration (float): The duration of the waveform in seconds.
            sample_rate (float): The sampling rate in samples per second.

        Returns:
            numpy.ndarray: The time axis as a numpy array.

        """

        return np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    

class StopWatch:
    def __init__(self):
        self._start = None
        self._stop = None
        self._elapsed = None

    def start(self):
        self._start = perf_counter()

    def stop(self):
        self._stop = perf_counter()
        self._elapsed = self._stop - self._start
        self._start = None
        self._stop = None
        return self._elapsed