from converter import *

def show_menu():
    print("=== Temperature Converter ===")
    print("1. Convert Temperature")
    print("2. Exit")

def convert_temp():
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid temperature input. Please enter a number.")
        return

    print("Choose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    elif choice == "5":
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F = {result:.2f}K")
    elif choice == "6":
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp}K = {result:.2f}°F")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    show_menu()
    while True:
        option = input("Choose an option (1 or 2): ")
        if option == "1":
            convert_temp()
            print()  # empty line
            show_menu()
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice.")
