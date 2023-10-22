people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 150
youngest_name = ""

for person in people:    
    person_list = person.split()

    name = person_list[0]
    age = int(person_list[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name
    
    #print(person_list)

print(f"The youngest is {youngest_name}, who is {youngest_age} years old. ")
