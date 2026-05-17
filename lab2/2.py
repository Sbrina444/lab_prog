import numpy as np
import matplotlib.pyplot as plt

def f(x):
    result = np.full_like(x, np.nan, dtype=float)
    mask1 = (x >= 0) & (x <= 1)
    result[mask1] = np.sqrt(x[mask1] + 1) - np.sqrt(x[mask1]) - 0.5
    mask2 = (x > 1) & (x <= 2)
    result[mask2] = np.exp(-x[mask2] - 1/x[mask2])
    return result

x = np.linspace(0, 2, 1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

x_break = 1
y_left = np.sqrt(2) - 1 - 0.5
y_right = np.exp(-2)

plt.plot(x_break, y_left, 'ro', markersize=8, label=f'Левая граница: {y_left:.4f}')
plt.plot(x_break, y_right, 'go', markersize=8, label=f'Правая граница: {y_right:.4f}')

plt.annotate('Точка разрыва\n(скачок функции)',
             xy=(x_break, y_left),
             xytext=(1.3, -0.2),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График функции', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(0, 2)
plt.ylim(-0.5, 0.6)

plt.tight_layout()
plt.show()