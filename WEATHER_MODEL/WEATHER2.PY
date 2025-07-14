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

print(f"\nQuadratic model: y = {a:.3f}x² + {b:.3f}x + {c:.3f}\n")

# Function to predict temperature
def predict_temperature(hour):
    return a*hour**2 + b*hour + c

# Get user input
while True:
    try:
        hour = int(input("Enter hour of the day (0–23) to predict temperature: "))
        if 0 <= hour <= 23:
            predicted_temp = predict_temperature(hour)
            print(f"Predicted temperature at {hour:02d}:00 is {predicted_temp:.2f}°C\n")
        else:
            print("⚠️ Please enter a valid hour between 0 and 23.")
    except ValueError:
        print("⚠️ Invalid input. Please enter an integer.")
    
    another = input("Do you want to predict another hour? (y/n): ").strip().lower()
    if another != 'y':
        print("Exiting weather forecast model. Goodbye!")
        break
