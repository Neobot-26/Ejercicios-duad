temp_fahrenheit=0
temp_kelvin=0
temp_celsius=int(input("Enter temperature in Celsius degrees:"))
temp_fahrenheit=(temp_celsius*1.8)+32
temp_kelvin=temp_celsius+273.15
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")
print(f"{temp_celsius}°C is equal to {temp_kelvin} K")