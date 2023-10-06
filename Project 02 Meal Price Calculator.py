child = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of an adults's meal? "))
countchild = int(input("How many children are there? "))
countadult = int(input("How many adults are there? "))
subtotal = child * countchild + adult * countadult
print(f"Subtotal: ${subtotal:.2f}")

taxrate = float(input("Enter the sales tax rate: "))
tax = subtotal * taxrate / 100
print(f"Sales Tax: ${tax:.2f}")

total = subtotal + tax
print(f"Total: ${total:.2f}")

payment = float(input("Enter the payment amount: "))
change = payment - total
print(f"Change: ${change:.2f}")

# Extra work: Donation Request
charity = "Thank you, your change was donated to charity." 
returnchange = "Here is your change."

donate = input("Would you like to donate the change to charity? Y/N: ").lower() 
if donate == 'y':
    print(charity)
else:
    print(returnchange)