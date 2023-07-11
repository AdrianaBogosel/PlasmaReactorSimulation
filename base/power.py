import numpy as np
import matplotlib.pyplot as plt

def getLissajousCurve():
    # Parameters for the Lissajous equation
    A = 1.5  # Amplitude of the x-axis oscillation
    B = 1.5  # Amplitude of the y-axis oscillation
    a = 6.0  # Angular frequency along the x-axis
    b = 6.0  # Angular frequency along the y-axis
    delta = np.pi / 21  # Phase difference

    # Generate time values
    t = np.linspace(0, 2 * np.pi, 10_000)

    # Calculate the x and y coordinates based on the Lissajous equation
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    rand = np.random.randn(int(1e6 * 1e-2)) * 0.005

    # Plot the Lissajous curve
    plt.cla()
    plt.plot(x + rand, y)
    plt.xlabel('Voltage [kV]')
    plt.ylabel('Charge [C]')
    plt.title('Lissajous Curve')
    plt.grid(True)
    plt.savefig("plots/lissajous.png")
