import sympy

class Capacitor:
    """
    Represents a capacitor and its properties.

    Methods:
    - __init__(vale: float, symbol: str): Initialize a Capacitor instance.
    - getValue(): Get the value of the capacitor.
    - getSymbol(): Get the symbol representing the capacitor.

    Note: This class assumes the existence of the sympy library.
    """
    def __init__(self, vale : float, symbol : str) -> None:
        """
        Initialize a Capacitor instance.

        Parameters:
        - vale (float): Value of the capacitor.
        - symbol (str): Symbol representing the capacitor.

        Returns:
        None

        This method initializes a Capacitor instance with the provided value and symbol.

        Note: This method assumes the existence of the sympy library.
        """
        self.__value = vale
        self.__symbol = sympy.Symbol(symbol)

    def getValue(self):
        """
        Get the value of the capacitor.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The value of the capacitor.

        This method returns the value of the capacitor. It is used to retrieve the value of the capacitor.

        Note: This method assumes the existence of the sympy library.
        """
        return self.__value
    
    def getSymbol(self):
        """
        Get the symbol representing the capacitor.

        Parameters:
        - self: The instance of the class calling this method.

        Returns:
        The symbol representing the capacitor.

        This method returns the symbol that represents the capacitor. It is used to retrieve the symbol representing the capacitor.

        Note: This method assumes the existence of the sympy library.
        """
        return self.__symbol