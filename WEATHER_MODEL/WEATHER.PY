import numpy as np

# Data points (hour, temperature)
x1, y1 = 6, 20
x2, y2 = 12, 32
x3, y3 = 20, 22

# Set up the system of equations:
# a*x^2 + b*x + c = y
A = np.array([
    [x1**2, x1, 1],
    [x2**2, x2, 1],
    [x3**2, x3, 1]
])

Y = np.array([y1, y2, y3])

# Solve for [a, b, c]
coefficients = np.linalg.solve(A, Y)
a, b, c = coefficients

print(f"Quadratic model: y = {a:.3f}x² + {b:.3f}x + {c:.3f}")

# Function to predict temperature
def predict_temperature(hour):
    return a*hour**2 + b*hour + c

# Example: predict temperature at 16:00 (4 PM)
hour = 12
predicted_temp = predict_temperature(hour)
print(f"Predicted temperature at {hour}:00 is {predicted_temp:.2f}°C")

# Optional: predict for all hours and print
print("\nHourly Forecast:")
for h in range(0, 24):
    temp = predict_temperature(h)
    print(f"{h:02d}:00 → {temp:.2f}°C")
