loansize = int(input("How large is the loan?"))
credithist = int(input("How good is your credit history?"))
income = int(input("How high is your income?"))
downpayment = int(input("How large is your down payment?"))

decision = False

if loansize >= 5:
    if credithist >= 7 and income >= 7:
        decision = True
    elif credithist >= 7 or income >= 7:
        if downpayment >= 5:
            decision = True
        else:
            decision = False
    else:  # need to set to false if the parent condition is not met
        decision = False

else:
    if credithist < 4:
        decision = False
    else:
        if income >= 7 or downpayment >= 7:
            decision = True
        elif income >= 4 and downpayment >= 4:
            decision = True
        else:
            decision = False
print(decision)
