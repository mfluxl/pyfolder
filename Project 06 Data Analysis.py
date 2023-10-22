
### Final Project -  Life Expectancy - Matheus Felber ###

lowest = float('inf')
highest = float('-inf')

year_low = None
year_high = None
country_low = None
country_high = None

user_country_lowest = None
user_country_highest = None
user_year_low = None
user_year_high = None

with open("life-expectancy.csv") as dataset:
    next(dataset)

    print("Welcome!\nYou can find:\nThe mininimum and maximum life expectancies for a country of your choice") #extra mile
    print("And for any given year:\nThe average life expectancy\nThe country with the minimum life expectancy\nThe country with maximum life expectancy") #project
    

    user_input_year = int(input("Enter a year: "))

    user_country = str(input("Type a country: ")).title()

    

    for line in dataset:
        clear_line = line.strip()
        clearlist = clear_line.split(",")
        country = clearlist[0]
        year = clearlist[2]
        age = float(clearlist[3])

        if age <= lowest:
            lowest = age
            year_low = year
            country_low = country
            
        if age >= highest:
            highest = age
            year_high = year
            country_high = country

        if user_country == country:                 
            if user_country_lowest is None or age <= user_country_lowest:         
                user_country_lowest = age
                user_year_low = year             
            if user_country_highest is None or age >= user_country_highest:      
                user_country_highest = age
                user_year_high = year

    if user_country_lowest is None and user_country_highest is None:
        print(f"Invalid command! No data found for the country {user_country}")
    else:
        print(f"\nThe country chosen was {user_country}:\nLowest Life Expectancy: {user_country_lowest:.2f} (Year {user_year_low})\nHighest Life Expectancy: {user_country_highest:.2f} (Year {user_year_high})")

    print(f"\nLowest value for life expectancy in the world: {lowest:.2f}\nCountry: {country_low} (Year {year_low})")
    print(f"\nHighest value for life expectancy in the world: {highest:.2f}\nCountry: {country_high} (Year {year_high})")

   
    total_age = 0
    count = None
    for line in dataset:
        clear_line = line.strip()
        clearlist = clear_line.split(",")
        year = clearlist[2]
        age = float(clearlist[3])

        if year == user_input_year:
            total_age += age
            count += 1

        if count == None:
            print(f"Year not listed!")
        else:
            average_age = total_age / count
            print(f"\nAverage Life Expectancy for {user_input_year}: {average_age}")

        
            min_age_country = ""
            max_age_country = ""
            min_age = float('inf')
            max_age = float('-inf')

            dataset.seek(0)  

            for line in dataset:
                clear_line = line.strip()
                clearlist = clear_line.split(",")
                year = clearlist[2]
                age = float(clearlist[3])
                current_country = clearlist[0]

                if year == user_input_year:
                    if age < min_age:
                        min_age = age
                        min_age_country = current_country
                    if age > max_age:
                        max_age = age
                        max_age_country = current_country

        print(f"Country with the Minimum Life Expectancy for {user_input_year}: {min_age_country} ({min_age:.2f})")
        print(f"Country with the Maximum Life Expectancy for {user_input_year}: {max_age_country} ({max_age:.2f})")


       
       #if user_country not in dataset:
       #     print("Please enter a country: ")
   # print(f"Lowest and highest value for life expectancy in the world:\nLowest:{lowest}. Highest: {highest}\n")
   # print(f"The country chosen was {user_country}:\nLowest Life Expectancy: {user_country_lowest}.\nHighest Life Expectancy: {user_country_highest}")
