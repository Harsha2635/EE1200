import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 5  # Amplitude
omega = 2 * np.pi  # Angular frequency
delta = np.radians(90)  # Phase shift in radians
t = np.linspace(0, 10 * np.pi / omega, 1000)  # Time values for multiple cycles

# Parametric equations
x = A * np.sin(omega * t)  # x = A * sin(ωt)
y = A * np.sin(2 * omega * t + delta)  # y = A * sin(2ωt + δ)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel("x = A*sin(ωt)")
plt.ylabel("y = -A*cos(2ωt)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.axis('equal')
plt.show()

