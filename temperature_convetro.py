def celsius(x, temperature):
    match x:
        case 1:
            print("The temperature doesn't change!")
        case 2:
            print(f"{temperature}°C to Fahrenheit (°F) = {(temperature * 9/5) + 32:.2f}°F")
        case 3:
            print(f"{temperature}°C to Kelvin (K) = {temperature + 273.15:.2f}K")

def fahrenheit(x, temperature):
    match x:
        case 1:
            print("The temperature doesn't change!")
        case 2:
            print(f"{temperature}°F to Celsius (°C) = {(temperature - 32) * 5/9:.2f}°C")
        case 3:
            print(f"{temperature}°F to Kelvin (K) = {(temperature - 32) * 5/9 + 273.15:.2f}K")

def kelvin(x, temperature):
    match x:
        case 1:
            print("The temperature doesn't change!")
        case 2:
            print(f"{temperature}K to Celsius (°C) = {temperature - 273.15:.2f}°C")
        case 3:
            print(f"{temperature}K to Fahrenheit (°F) = {(temperature - 273.15) * 9/5 + 32:.2f}°F")
def main():
    print("This is the TEMPERATURE CONVERTER PROJECT, made by tevoshw, 06/02/2025\n")
    print("""
    Select the TEMPERATURE UNIT to be CONVERTED!
    
    1 - Celsius
    2 - Fahrenheit
    3 - Kelvin
    """)

    while True:
        try:
            user_input_to_be_converted = int(input("\nEnter the number of your choice: "))
            if user_input_to_be_converted not in [1, 2, 3]:
                print("Invalid option, try again!")
                continue

            user_input_temperature = float(input("Enter the temperature: "))

            print("""\nNow select the target temperature unit:
            
            1 - Celsius
            2 - Fahrenheit
            3 - Kelvin
            """)

            user_input_will_convert = int(input("Enter the number of your choice: "))
            if user_input_will_convert not in [1, 2, 3]:
                print("Invalid option, try again!")
                continue

            match user_input_to_be_converted:
                case 1:
                    celsius(user_input_will_convert, user_input_temperature)
                    break
                case 2:
                    fahrenheit(user_input_will_convert, user_input_temperature)
                    break
                case 3:
                    kelvin(user_input_will_convert, user_input_temperature)
                    break

        except ValueError:
            print("Invalid input, please enter a number.")

main()
