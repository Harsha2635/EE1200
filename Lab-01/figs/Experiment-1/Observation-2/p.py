import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude
omega = 2 * np.pi  # Angular frequency
t = np.linspace(0, 2 * np.pi, 1000)  # Time values

# Parametric equations
x = A * np.sin(omega * t)
y = A * np.sin(omega * t)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title("Parametric Plot: x = A*sin(ωt), y = A*sin(ωt)")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.axis('equal')
plt.show()

