import numpy as np
import pandas as pd

# Step 1: Read data from Excel
data = pd.read_excel("weather_data.xlsx")

# Extract data points
x_vals = data['Hour'].values
y_vals = data['Temperature'].values

if len(x_vals) != 3:
    print("⚠️ Error: Excel file must have exactly 3 data points.")
    exit()

x1, y1 = x_vals[0], y_vals[0]
x2, y2 = x_vals[1], y_vals[1]
x3, y3 = x_vals[2], y_vals[2]

# Step 2: Set up the system of equations
A = np.array([
    [x1**2, x1, 1],
    [x2**2, x2, 1],
    [x3**2, x3, 1]
])

Y = np.array([y1, y2, y3])

# Step 3: Solve for [a, b, c]
coefficients = np.linalg.solve(A, Y)
a, b, c = coefficients

print(f"\n✅ Model derived from Excel data: y = {a:.3f}x² + {b:.3f}x + {c:.3f}\n")

# Function to predict temperature
def predict_temperature(hour):
    return a*hour**2 + b*hour + c

# Step 4: User input loop
while True:
    try:
        hour = int(input("Enter hour of the day (0–23) to predict temperature: "))
        if 0 <= hour <= 23:
            predicted_temp = predict_temperature(hour)
            print(f"🌡️ Predicted temperature at {hour:02d}:00 is {predicted_temp:.2f}°C\n")
        else:
            print("⚠️ Please enter a valid hour between 0 and 23.")
    except ValueError:
        print("⚠️ Invalid input. Please enter an integer.")
    
    another = input("Do you want to predict another hour? (y/n): ").strip().lower()
    if another != 'y':
        print("👋 Exiting weather forecast model. Goodbye!")
        break
