


with open("hr_system.txt") as text_file:
    for lines in text_file:
        no_spaces = lines.strip()
        listed_items = lines.split(" ")
            
        name = listed_items[0]
        id = listed_items[1]
        job_title = listed_items[2]
        salary = float(listed_items[3])

        pay = salary / 24

        if job_title.lower() == "engineer":
            pay += 1000


        print(f"{name} (ID: {id}), {job_title} - ${pay:.2f}")

