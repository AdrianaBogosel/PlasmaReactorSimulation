from datetime import datetime
from pathlib import Path
import os

class bcolors:
    """
    Provides color codes for console output.

    Attributes:
    - HEADER
    - OKBLUE
    - OKGREEN
    - OKYELLOW
    - OKRED
    - ENDC
    - BOLD
    - UNDERLINE

    Note: This class is used for console output formatting.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class LoggerIfc:
    """
    Provides logging functionality with different log levels.

    Methods:
    - __init__(componentName: str): Initialize a LoggerIfc instance.
    - debug(msg: str): Log a debug message.
    - info(msg: str): Log an info message.
    - warning(msg: str): Log a warning message.
    - error(msg: str): Log an error message.
    - critical(msg: str): Log a critical message.
    - save(path: str, filename: str): Save the log messages to a file.

    Note: This class assumes the existence of the datetime, pathlib, and os libraries.
    """
    def __init__(self, componentName : str) -> None:
        """
        Initialize a LoggerIfc instance.

        Parameters:
        - componentName: The name of the component for logging.

        Returns:
        None

        This method initializes a LoggerIfc instance with the provided component name. It also sets up an empty backlog list
        to store the logged messages.

        Note: This method assumes the existence of the datetime and pathlib libraries.
        """
        self.name = componentName
        self.backlogLst = []

    def __del__(self) -> None:
        """
        Clean up the LoggerIfc instance.

        Parameters:
        None

        Returns:
        None

        This method clears the backlog list of logged messages when the instance is deleted.

        Note: This method assumes the existence of the pathlib library.
        """
        self.backlogLst.clear()

    def __log(self, msg : str, level : str) -> str:
        """
        Format the log message with the appropriate level and timestamp.

        Parameters:
        - msg: The log message to be formatted.
        - level: The log level of the message.

        Returns:
        The formatted log message.

        This method takes a log message, adds the appropriate log level and timestamp, and formats the message with color codes
        for console output.

        Note: This method assumes the existence of the datetime and bcolors classes.
        """
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if level == "INFO":
            return f"{bcolors.OKGREEN}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"
        elif level == "WARNING":
            return f"{bcolors.OKYELLOW}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"
        elif level == "ERROR":
           return f"{bcolors.OKRED}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"
        elif level == "DEBUG":
            return f"{bcolors.OKBLUE}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"
        elif level == "CRITICAL":
           return f"{bcolors.OKRED}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"
        else:
            return f"{bcolors.OKBLUE}{dt_string} [{level}] {self.name}: {msg}{bcolors.ENDC}"

    def debug(self, msg : str) -> None:
        """
        Log a debug message.

        Parameters:
        - msg: The debug message to be logged.

        Returns:
        None

        This method logs a debug message with the appropriate log level and timestamp. The message is added to the backlog list
        and printed to the console.

        Note: This method assumes the existence of the bcolors class.
        """
        self.backlogLst.append(self.__log(msg, "DEBUG"))
        print(self.backlogLst[-1])

    def info(self, msg : str) -> None:
        """
        Log a debug message.

        Parameters:
        - msg: The debug message to be logged.

        Returns:
        None

        This method logs a debug message with the appropriate log level and timestamp. The message is added to the backlog list
        and printed to the console.

        Note: This method assumes the existence of the bcolors class.
        """
        self.backlogLst.append(self.__log(msg, "INFO"))
        print(self.backlogLst[-1])

    def warning(self, msg : str) -> None:
        """
        Log a warning message.

        Parameters:
        - msg: The warning message to be logged.

        Returns:
        None

        This method logs a warning message with the appropriate log level and timestamp. The message is added to the backlog
        list and printed to the console.

        Note: This method assumes the existence of the bcolors class.
        """
        self.backlogLst.append(self.__log(msg, "WARNING"))
        print(self.backlogLst[-1])

    def error(self, msg : str) -> None:
        """
        Log an error message.

        Parameters:
        - msg: The error message to be logged.

        Returns:
        None

        This method logs an error message with the appropriate log level and timestamp. The message is added to the backlog
        list and printed to the console.

        Note: This method assumes the existence of the bcolors class.
        """
        self.backlogLst.append(self.__log(msg, "ERROR"))
        print(self.backlogLst[-1])

    def critical(self, msg : str) -> None:
        """
        Log a critical message.

        Parameters:
        - msg: The critical message to be logged.

        Returns:
        None

        This method logs a critical message with the appropriate log level and timestamp. The message is added to the backlog
        list and printed to the console.

        Note: This method assumes the existence of the bcolors class.
        """
        self.backlogLst.append(self.__log(msg, "CRITICAL"))
        print(self.backlogLst[-1])

    def save(self, path : str, filename : str) -> None:
        """
        Save the log messages to a file.

        Parameters:
        - path: The directory path to save the log file.
        - filename: The filename of the log file.

        Returns:
        None

        This method saves the logged messages to a file with the provided directory path and filename. If the path does not
        exist, it logs an error and creates a local copy in the current working directory.

        Note: This method assumes the existence of the pathlib and os libraries.
        """
        if Path(path).exists() == False:
            self.error(f"Path {path} doesn't exists. Creating local copy!")
            path = os.getcwd()
        
        with open(os.path.join(path, filename), "w+") as f:
            for line in self.backlogLst:
                f.write(line + "\n")
        self.backlogLst.clear()