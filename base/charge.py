import sympy
from utility.logger import LoggerIfc
from reactor.capacitor import Capacitor
from reactor.ac_voltage_source import VoltageSource
from matplotlib import pyplot as plt
import numpy as np

class Charge:
    """
    Represents a charge entity and its related calculations.

    Methods:
    - __init__(symbol: str, voltageSource: VoltageSource, capacitance: Capacitor): Initialize an instance of the Charge class.
    - getSymbol(): Get the symbol representing the charge.
    - getEquation(): Get the equation representing the charge.
    - getRhsEquation(): Get the right-hand side of the equation representing the charge.
    - plotLissajousCurve(amplitudeXAsixOscillation=1.5, amplitudeYAsixOscillation=1.5, angularFrequencyX=6, angularFrequencyY=6, phaseDifference=np.pi/21): Plot a Lissajous curve based on the given parameters.

    Note: This class assumes the existence of LoggerIfc, VoltageSource, Capacitor, numpy, and matplotlib classes.
    """
    def __init__(self, symbol : str, voltageSource : VoltageSource, capacitance : Capacitor):
        """
        Initialize an instance of the Charge class.

        Parameters:
        - self: The instance of the class being initialized.
        - symbol: The symbol representing the charge (e.g., 'Q', 'C').
        - voltageSource: An instance of the VoltageSource class representing the voltage source.
        - capacitance: An instance of the Capacitor class representing the capacitance.

        Returns:
        None

        This method initializes an instance of the Charge class. It assigns a symbol to the charge and sets up an equation using
        the provided voltage source and capacitance. The equation relates the charge symbol to the product of the voltage source
        symbol and the capacitance symbol.

        Note: This method assumes the existence of a LoggerIfc class and the imported sympy library.
        """
        t = sympy.Symbol('t')
        self.__symbol = sympy.Function(symbol)(t)
        self.__log = LoggerIfc("Charge")
        self.__equation = sympy.Eq(self.__symbol, voltageSource.getSymbol() * capacitance.getSymbol())

        self.__log.debug("Charge created with symbol: " + str(self.__symbol) + " and equation: " + str(self.__equation))

    def getSymbol(self):
        """
        Get the symbol representing the charge.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The symbol representing the charge.

        This method returns the symbol that represents the charge. It is used to retrieve the value of the charge symbol.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug(f"Symbol: {self.__symbol}")
        return self.__symbol

    def getEquation(self):
        """
        Get the equation representing the charge.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The equation representing the charge.

        This method returns the equation that represents the charge. It is used to retrieve the equation related to the charge,
        which has been previously set during initialization.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug(f"Equation: {self.__equation}")
        return self.__equation
    
    def getRhsEquation(self):
        """
        Get the right-hand side of the equation representing the charge.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The right-hand side of the equation representing the charge.

        This method returns the right-hand side of the equation that represents the charge. It is used to retrieve only the
        right-hand side of the equation, excluding the left-hand side.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug(f"RHS of equation: {self.__equation.rhs}")
        return self.__equation.rhs

    def plotLissajousCurve(self, amplitudeXAsixOscillation = 1.5, amplitudeYAsixOscillation = 1.5, angularFrequencyX = 6, angularFrequencyY = 6, phaseDifference = np.pi / 21):
        """
        Plot a Lissajous curve based on the given parameters.

        Parameters:
        - self: The instance of the class containing this method.
        - amplitudeXAsixOscillation (optional): The amplitude of the X-axis oscillation (default: 1.5).
        - amplitudeYAsixOscillation (optional): The amplitude of the Y-axis oscillation (default: 1.5).
        - angularFrequencyX (optional): The angular frequency of the X-axis oscillation (default: 6).
        - angularFrequencyY (optional): The angular frequency of the Y-axis oscillation (default: 6).
        - phaseDifference (optional): The phase difference between the X and Y oscillations (default: pi/21).

        Returns:
        None

        This function plots a Lissajous curve based on the provided parameters. It uses the Lissajous equation to calculate the
        X and Y coordinates of the curve and then plots it using Matplotlib. The resulting plot is saved as 'lissajous.png' in the
        'plots' directory.

        Note: This function requires the 'numpy' and 'matplotlib' libraries to be installed.
        """
        self.__log.debug("Plotting Lissajous curve with parameters: amplitudeXAsixOscillation = " + str(amplitudeXAsixOscillation) + ", amplitudeYAsixOscillation = " + str(amplitudeYAsixOscillation) + ", angularFrequencyX = " + str(angularFrequencyX) + ", angularFrequencyY = " + str(angularFrequencyY) + ", phaseDifference = " + str(phaseDifference))
        timeValues = np.linspace(0, 2 * np.pi, 10_000)

        # Calculate the x and y coordinates based on the Lissajous equation
        x = amplitudeXAsixOscillation * np.sin(angularFrequencyX * timeValues + phaseDifference)
        y = amplitudeYAsixOscillation * np.sin(angularFrequencyY * timeValues)

        rand = np.random.randn(int(1e6 * 1e-2)) * 0.005

        # Plot the Lissajous curve
        plt.cla()
        plt.plot(x + rand, y)
        plt.xlabel('Voltage [kV]')
        plt.ylabel('Charge [C]')
        plt.title('Lissajous Curve')
        plt.grid(True)
        plt.savefig("plots/lissajous.png")
