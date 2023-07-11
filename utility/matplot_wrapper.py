from matplotlib import pyplot as plt
from utility.time import Time
from utility.noise import NoiseGenerator

class MatPlotWrapper:
    def __init__(self, plotDuration, plotSamples) -> None:
        self.__time = Time().getTimeAxis(plotDuration, plotSamples)
        self.__noise = NoiseGenerator()
        self.__plotDuration = plotDuration
        self.__plotSamples = plotSamples

    def plotInstance(self, instance, title : str, ylabel : str, addNoiseLevel : float = 1):
        plt.cla()
        plt.plot(self.__time * 1e3, instance + self.__noise.getNoise(self.__plotDuration, self.__plotSamples, addNoiseLevel))
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel("Time (ms)")
        plt.grid(True)
        plt.savefig(f"plots/{title}.png")

    def getTime(self):
        return self.__time