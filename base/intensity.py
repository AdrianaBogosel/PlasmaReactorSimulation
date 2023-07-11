from utility.logger import LoggerIfc
import sympy
import numpy as np
from base.charge import Charge
from reactor.ac_voltage_source import VoltageSource

class Intensity:
    """
    Represents the intensity of a current and its related calculations.

    Methods:
    - __init__(qt: Charge): Initialize an instance of the Intensity class.
    - getSymbol(): Get the symbol representing the intensity.
    - getEquation(): Get the equation representing the intensity.
    - getRhsEquation(): Get the right-hand side of the equation representing the intensity.
    - substituteCharge(qt: Charge): Substitute the charge in the intensity equation.
    - substituteVoltage(vt: VoltageSource): Substitute the voltage in the intensity equation.
    - substituteCapacitance(capacitance: float): Substitute the capacitance in the intensity equation.
    - solve(time: np.ndarray): Solve the intensity equation for the given time values.
    - getSolutions(): Get the solved intensity values.

    Note: This class assumes the existence of LoggerIfc, Charge, and VoltageSource classes.
    """
    def __init__(self, qt : Charge):
        """
        Initialize an instance of the Intensity class.

        Parameters:
        - qt: An instance of the Charge class representing the charge.

        Returns:
        None

        This method initializes an instance of the Intensity class. It sets up the intensity symbol and equation based on
        the provided charge. The equation is derived from the time derivative of the charge symbol.

        Note: This method assumes the existence of a LoggerIfc class and the imported sympy and numpy libraries.
        """
        self.__log = LoggerIfc("Intensity")
        t = sympy.Symbol('t')
        self.__symbol = sympy.Function("i")(t)
        self.__equation = sympy.Eq(self.__symbol, sympy.Derivative(qt.getSymbol(), t))
        self.__log.debug("Intensity created with symbol: " + str(self.__symbol) + " and equation: " + str(self.__equation))
        self.__solutions = None
        self.__data = None

    def getSymbol(self):
        """
        Get the symbol representing the intensity.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The symbol representing the intensity.

        This method returns the symbol that represents the intensity. It is used to retrieve the value of the intensity symbol.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("Symbol: " + str(self.__symbol))
        return self.__symbol
    
    def getEquation(self):
        """
        Get the equation representing the intensity.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The equation representing the intensity.

        This method returns the equation that represents the intensity. It is used to retrieve the equation related to the intensity.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("Equation: " + str(self.__equation))
        return self.__equation
    
    def getRhsEquation(self):
        """
        Get the right-hand side of the equation representing the intensity.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The right-hand side of the equation representing the intensity.

        This method returns the right-hand side of the equation that represents the intensity. It is used to retrieve only the
        right-hand side of the equation, excluding the left-hand side.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("RHS of equation: " + str(self.__equation.rhs))
        return self.__equation.rhs
    
    def substituteCharge(self, qt : Charge):
        """
        Substitute the charge in the intensity equation.

        Parameters:
        - self: The instance of the class calling this method.
        - qt: An instance of the Charge class representing the charge to be substituted.

        Returns:
        None

        This method substitutes the charge symbol in the intensity equation with the provided charge's equation. It updates
        the intensity equation accordingly.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("Substituting charge: " + str(qt.getSymbol()))
        self.__equation = self.__equation.subs(qt.getSymbol(), qt.getEquation().rhs)
        self.__log.debug("New equation: " + str(self.__equation))
    
    def substituteVoltage(self, vt : VoltageSource):
        """
        Substitute the voltage in the intensity equation.

        Parameters:
        - self: The instance of the class calling this method.
        - vt: An instance of the VoltageSource class representing the voltage to be substituted.

        Returns:
        None

        This method substitutes the voltage symbol in the intensity equation with the provided voltage's equation. It updates
        the intensity equation accordingly.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("Substituting voltage: " + str(vt.getSymbol()))
        self.__equation = self.__equation.subs(vt.getSymbol(), vt.getEquation())
        self.__log.debug("New equation: " + str(self.__equation))

    def substituteCapacitance(self, capacitance : float):
        """
        Substitute the capacitance in the intensity equation.

        Parameters:
        - self: The instance of the class calling this method.
        - capacitance: The capacitance value to be substituted.

        Returns:
        None

        This method substitutes the capacitance symbol in the intensity equation with the provided capacitance value. It updates
        the intensity equation accordingly.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        self.__log.debug("Substituting capacitance: " + str(capacitance))
        self.__equation = self.__equation.subs("C_cell", capacitance)
        self.__log.debug("New equation: " + str(self.__equation))

    def solve(self, time : np.ndarray):
        """
        Solve the intensity equation for the given time values.

        Parameters:
        - self: The instance of the class calling this method.
        - time: An array of time values.

        Returns:
        An array of solved intensity values.

        This method solves the intensity equation for the given time values. It evaluates the equation for each time value
        and stores the solutions. The solved intensity values are then returned.

        Note: This method assumes the existence of a LoggerIfc class and the imported sympy and numpy libraries.
        """
        self.__log.debug("Solving equation: " + str(self.__equation))
        self.__solutions = [sympy.solve(equation) for equation in [self.__equation.subs("t", t) for t in time]]
        self.__data = [next(iter(sol[0].values())) * 1e3 for sol in self.__solutions]
        return self.__data

    def getSolutions(self):
        """
        Get the solved intensity values.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The solved intensity values.

        This method returns the previously solved intensity values. It is used to retrieve the results of the intensity equation
        after it has been solved.

        Note: This method assumes the existence of a LoggerIfc class.
        """
        return self.__data