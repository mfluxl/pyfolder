number_list = []

stop_typing = False
sum = 0
largest = -1


while not stop_typing:
    ask = float(input("Pick a number: "))

    if ask > largest:
        largest = ask

    if ask == 0:
        stop_typing = True
        print(number_list)
        
        print(f"The sum is {sum:.3f}")
        print(f"The largest number is {largest}")

    number_list.append(ask)
    sum += ask






