# Temperature Converter
def temperature_converter(temp, unit:str):
    if "F" in unit:
        return  (temp - 32) / 1.8
    elif "C" in unit:
        return (temp * 9/5) + 32

print(temperature_converter(77 , "F"))

