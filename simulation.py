from reactor.ac_voltage_source import VoltageSource as Vs
from reactor.reactor import Reactor
from reactor.capacitor import Capacitor
from utility.logger import LoggerIfc
from utility.time import Time

log = LoggerIfc("Simulation")
log.info("Simulation started.")

vs = Vs(6000, 910)
C_cell = Capacitor(1.347e-9, "C_cell")
C_barrier = Capacitor(2.13e-9, "C_barrier")
C_gap = Capacitor(3.660e-9, "C_gap")

reactor = Reactor(C_cell, C_barrier, C_gap ,vs)
reactor.simulateWithPlots(1e-2, 1e5)
log.info("Simulation ended.")
