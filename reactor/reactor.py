import sympy
from reactor.capacitor import Capacitor
from utility.logger import LoggerIfc
from reactor.ac_voltage_source import VoltageSource as Vs
from base.charge import Charge
from base.intensity import Intensity
from utility.matplot_wrapper import MatPlotWrapper
from utility.job_scheduler import JobScheduler


class Reactor:
    """
    Represents a reactor and its simulation.

    Methods:
    - __init__(reactorCellCapacitor: Capacitor, dielectricBarrierCapacitor: Capacitor, plasmaGapCapacitor: Capacitor, voltageSrc: Vs): Initialize a Reactor instance.
    - simulateWithPlots(duration: float = 1e-1, samplePoint: float = 1e-6): Simulate the reactor with plots.

    Note: This class assumes the existence of LoggerIfc, Capacitor, Vs, Charge, Intensity, JobScheduler, and MatPlotWrapper classes.
    """
    def __init__(self, reactorCellCapacitor: Capacitor, dielectricBarrierCapacitor: Capacitor, plasmaGapCapacitor: Capacitor, voltageSrc: Vs):
        """
        Initialize a Reactor instance.

        Parameters:
        - reactorCellCapacitor: An instance of the Capacitor class representing the reactor cell capacitor.
        - dielectricBarrierCapacitor: An instance of the Capacitor class representing the dielectric barrier capacitor.
        - plasmaGapCapacitor: An instance of the Capacitor class representing the plasma gap capacitor.
        - voltageSrc: An instance of the Vs class representing the voltage source.

        Returns:
        None

        This method initializes a Reactor instance with the provided capacitors and voltage source. It also creates a Charge
        instance and an Intensity instance for the simulation.

        Note: This method assumes the existence of a LoggerIfc, Capacitor, Vs, Charge, and Intensity classes.
        """
        self.log = LoggerIfc("Reactor")

        self.__reactorCellCapacitor = reactorCellCapacitor
        self.log.info(f"Reactor cell capacitance was added with value {self.__reactorCellCapacitor.getValue()}C and symbol {self.__reactorCellCapacitor.getSymbol()}")

        self.__dielectricBarrierCapacitor = dielectricBarrierCapacitor
        self.log.info(f"Dielectric barrier capacitance was added with value {self.__dielectricBarrierCapacitor.getValue()}C and symbol {self.__dielectricBarrierCapacitor.getSymbol()}")

        self.__plasmaGapCapacitor = plasmaGapCapacitor
        self.log.info(f"Plasma gap capacitance was added with value {self.__plasmaGapCapacitor.getValue()}C and symbol {self.__plasmaGapCapacitor.getSymbol()}")

        self.__voltageSrc = voltageSrc
        self.log.info(f"Voltage source was added with amplitude {self.__voltageSrc.getAmplitude()}V and frequency {self.__voltageSrc.getFrequency()}Hz")

        self.__charge = Charge("Q", self.__voltageSrc, self.__reactorCellCapacitor)

        self.__intensityInstance = Intensity(self.__charge)
        self.__intensityInstance.substituteCharge(self.__charge)
        self.__intensityInstance.substituteVoltage(self.__voltageSrc)
        self.__intensityInstance.substituteCapacitance(self.__reactorCellCapacitor.getValue())
        self.__jobScheduler = JobScheduler()

    def simulateWithPlots(self, duration: float = 1e-1, samplePoint: float = 1e-6):
        """
        Simulate the reactor with plots.

        Parameters:
        - self: The instance of the class calling this method.
        - duration: The duration of the simulation in seconds (default: 0.1).
        - samplePoint: The sample point of the simulation in seconds (default: 1e-6).

        Returns:
        None

        This method simulates the reactor with the given duration and sample point. It schedules and runs the intensity and
        voltage source solvers using a JobScheduler. After the simulation, it plots the results using MatPlotWrapper.

        Note: This method assumes the existence of a LoggerIfc, Intensity, JobScheduler, and MatPlotWrapper classes.
        """
        self.log.info(f"Simulating with duration {duration}s and sample point {samplePoint}s")

        ploter = MatPlotWrapper(duration, samplePoint)
        self.__jobScheduler.schedule(self.__intensityInstance.solve, ploter.getTime())
        self.__jobScheduler.schedule(self.__voltageSrc.solve, ploter.getTime())
        self.__jobScheduler.run()
        
        self.log.info("Finished simulating syntetic data. Plotting results!")
        ploter.plotInstance(self.__intensityInstance.getSolutions(), "Intensity I(t)", "Intensity (mA)", 8e-1)
        ploter.plotInstance(self.__voltageSrc.getSolutions(), "Tension V(t)", "Tension (V)", 1e2)
        ploter.plotInstance([i*v*1e-3 for i,v in zip(self.__intensityInstance.getSolutions(), self.__voltageSrc.getSolutions())], "Power approximated P(t)", "Power (W)", 0)
        ploter.plotInstance([i*v*1e-3 for i,v in zip(self.__intensityInstance.getSolutions(), self.__voltageSrc.getSolutions())], "Power approximated P(t) with noise", "Power (W)", 2)
        self.__charge.plotLissajousCurve()