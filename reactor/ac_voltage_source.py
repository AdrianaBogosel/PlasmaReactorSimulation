import sympy
from utility.logger import LoggerIfc

class VoltageSource:
    """
    Represents a voltage source and its related calculations.

    Methods:
    - __init__(amplitude, frequency): Initialize a VoltageSource instance.
    - getEquation(): Get the equation representing the voltage waveform.
    - getSymbol(): Get the symbol representing the voltage waveform.
    - getAmplitude(): Get the amplitude of the voltage waveform.
    - getFrequency(): Get the frequency of the voltage waveform.
    - solve(time): Solve the equation for the voltage waveform for the given time values.
    - getSolutions(): Get the solved voltage values.

    Note: This class assumes the existence of LoggerIfc and sympy libraries.
    """
    def __init__(self, amplitude, frequency) -> None:
        """
        Initialize a VoltageSource instance.

        Parameters:
        - amplitude (float): Amplitude of the voltage waveform.
        - frequency (float): Frequency of the voltage waveform in Hz.

        Returns:
        None

        This method initializes a VoltageSource instance. It sets up the voltage waveform equation based on the provided
        amplitude and frequency.

        Note: This method assumes the existence of a LoggerIfc class and the imported sympy library.
        """
        self.__log = LoggerIfc("VoltageSource")
        self.__voltAmplitude = amplitude
        self.__voltFrequency = frequency
        self.__time = sympy.Symbol("t")
        self.__symbol = sympy.Symbol("V(t)")

        # Create the equation for the voltage waveform
        self.__voltEquation = self.__voltAmplitude * sympy.sin(self.__voltFrequency * self.__time)
        self.__log.debug("Voltage waveform created with symbol: " + str(self.__symbol) + " and equation: " + str(self.__voltEquation))
        self.__equation = sympy.Eq(self.__symbol, self.__voltEquation)

    def getEquation(self):
        """
        Get the equation representing the voltage waveform.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The equation representing the voltage waveform.

        This method returns the equation that represents the voltage waveform. It is used to retrieve the equation related
        to the voltage waveform.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__voltEquation

    def getSymbol(self):
        """
        Get the symbol representing the voltage waveform.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The symbol representing the voltage waveform.

        This method returns the symbol that represents the voltage waveform. It is used to retrieve the value of the voltage
        waveform symbol.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__symbol
    
    def getAmplitude(self):
        """
        Get the amplitude of the voltage waveform.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The amplitude of the voltage waveform.

        This method returns the amplitude of the voltage waveform. It is used to retrieve the value of the voltage waveform's
        amplitude.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__voltAmplitude
    
    def getFrequency(self):
        """
        Get the amplitude of the voltage waveform.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The amplitude of the voltage waveform.

        This method returns the amplitude of the voltage waveform. It is used to retrieve the value of the voltage waveform's
        amplitude.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__voltFrequency

    def solve(self, time):
        """
        Solve the equation for the voltage waveform for the given time values.

        Parameters:
        - self: The instance of the class calling this method.
        - time: An array of time values.

        Returns:
        An array of solved voltage values.

        This method solves the equation for the voltage waveform for the given time values. It evaluates the equation for each
        time value and stores the solutions. The solved voltage values are then returned.

        Note: This method assumes the existence of a LoggerIfc class and the imported sympy library.
        """
        self.__log.debug("Solving equation: " + str(self.__equation))
        self.__solutions = [sympy.solve(equation) for equation in [self.__equation.subs("t", t) for t in time]]
        self.__data = [item for sublist in self.__solutions for item in sublist]
        return self.__data

    def getSolutions(self):
        """
        Get the solved voltage values.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The solved voltage values.

        This method returns the previously solved voltage values. It is used to retrieve the results of the voltage waveform
        equation after it has been solved.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__data