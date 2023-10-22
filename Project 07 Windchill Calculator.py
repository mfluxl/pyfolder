# Project 07: Windchill Calculator

# V = wind speed
# T = air temperature

# WCT (Fahrenheit + MPH) = 35.74 + 0.6215 * T - 35.75 * V**0.16 + 0.4275 * T * V**0.16 
# WCT (Celsius + KM/h)   = 13.12 + 0.6215 * T - 11.37 * V**0.16 + 0.3965 * T * V**0.16

# wind speeds (MPH): 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
# wind speeds (KM/h): 8.1, 16.1, 24.1, 32.2, 40.2, 48.3, 56.3, 64.4, 72.4, 80.5, 88.5, 96.5


string_miles = "5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60"
string_kilometers = "8.1, 16.1, 24.1, 32.2, 40.2, 48.3, 56.3, 64.4, 72.4, 80.5, 88.5, 96.5"

speeds_in_mph = string_miles.split(",")
speeds_in_kmh = string_kilometers.split(",")


def windchill(temperature, unit):

        if unit == "F":
            for speed in speeds_in_mph:
                V = float(speed)
                T = user_temperature

                wct = 35.74 + 0.6215 * T - 35.75 * V**0.16 + 0.4275 * T * V**0.16
                print(f"At temperature {user_temperature}{unit_of_measure}, and wind speed {V:.1f}MPH, the windchill is: {wct:.2f}F")
        
        
        elif unit == "C":
            for speed in speeds_in_kmh:    
                V = float(speed)
                T = user_temperature

                wct = 13.12 + 0.6215 * T - 11.37 * V**0.16 + 0.3965 * T * V**0.16
                print(f"At temperature {user_temperature}{unit_of_measure}, and wind speed {V:.1f}KM/h, the windchill is: {wct:.2f}C")

        else:
             print("Enter a temperature then choose (F)ahrenheit or (C)elcius.")



user_temperature = float(input("Enter a temperature: "))
unit_of_measure = input("In Fahrenheit or Celcius? [F/C]: ").capitalize()

windchill(user_temperature, unit_of_measure)

