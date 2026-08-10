# Temperature Converter

def temperature_converter(temp, unit: str):
    unit = unit.strip().upper()
    if unit == "F":
        return (temp - 32) / 1.8
    elif unit == "C":
        return (temp * 9 / 5) + 32
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."

print(temperature_converter(77, "F"))
print(temperature_converter(25, "C"))
print(temperature_converter(100, "k"))

