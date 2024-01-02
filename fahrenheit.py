def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit_temperature = float(input("Введите температуру в градусах Фаренгейта: "))
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} градусов Фаренгейта равны {celsius_temperature:.2f} градусам Цельсия.")
