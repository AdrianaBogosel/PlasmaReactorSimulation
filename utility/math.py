import sympy

class Math:
    """
    Provides mathematical utility functions.

    Methods:
    - deriveSymbol(symbol: sympy.Symbol, function: sympy.Function) -> sympy.Expr: Calculate the derivative of a function with respect to a symbol.

    Note: This class assumes the existence of the sympy library.
    """
    @staticmethod
    def deriveSymbol(symbol : sympy.Symbol, function : sympy.Function) -> sympy.Expr:
        """
        Provides mathematical utility functions.

        Methods:
        - deriveSymbol(symbol: sympy.Symbol, function: sympy.Function) -> sympy.Expr: Calculate the derivative of a function with respect to a symbol.

        Note: T`his class assumes the existence of the sympy library.
        """
        return sympy.diff(function, symbol)