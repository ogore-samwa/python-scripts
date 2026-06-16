# Integer (Whole numbers)
voltage = 240
current = 15

# Float (Decimal numbers)
power_factor = 0.85
frequency = 49.95

# String (Text - must be in quotes)
app_name = "VoltSec Web App"
status_msg = "System Secure"

# Boolean (True or False logical states)
is_breaker_tripped = False
is_encrypted = True

# Multiplication (*) to find Apparent Power (S = V * I)
apparent_power_va = voltage * current  # 240 * 15 = 3600 VA

# Division (/) to convert to kilo-Volt-Amperes (kVA)
apparent_power_kva = apparent_power_va / 1000  # 3.6 kVA

# Addition (+) and Subtraction (-)
total_load = 1500 + 2400
voltage_drop = 240 - 232

# Displaying a basic text and numeric output
print(f"Welcome to {app_name}!")
print(f"The calculated apparent power is {apparent_power_kva} kVA.")

# Formatting decimals to 2 decimal places using ':.2f'
pi_value = 3.14159265
print(f"Pi rounded to two places: {pi_value:.2f}")

# Electrical Cable Sizing Safety Check
max_allowable_drop = 5.0  # 5% max drop under standard regulations
actual_drop = 3.4

if actual_drop > max_allowable_drop:
    print("ALERT: Voltage drop exceeds IET regulation thresholds!")
elif actual_drop == max_allowable_drop:
    print("WARNING: System is precisely at the maximum regulatory limit.")
else:
    print("STATUS: Cable sizing is safe and compliant.")

# Capturing text input
user_name = input("Enter your technician name: ")
print(f"Logged in: {user_name}")

# Capturing numeric input for calculation
input_volts = input("Enter measured line voltage (V): ")
# Convert the text string to a decimal number (float)
voltage_float = float(input_volts)

input_amps = input("Enter measured current (A): ")
# Convert the text string to a whole number (integer)
current_int = int(input_amps)

# Execute Math
calculated_watts = voltage_float * current_int
print(f"Active Power: {calculated_watts} Watts")


