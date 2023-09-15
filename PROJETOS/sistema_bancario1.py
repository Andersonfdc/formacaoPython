menu = """
[1] - Deposit
[2] - Draw
[3] - Extract
[4] - Exit

=> """
balance = 0
limit = 500
extract = ''
number_draw = 0 
LIMIT_DRAW = 3

while True:
    option = (input(menu))

    if option == '1':
        value = float(input("Enter the value deposit: "))

        if value > 0:
            balance += value
            extract += f"Deposit: $ {value: .2f}\n"
        else:
            print('Invalid value!')  

    elif option == '2':
        value = float(input("Enter the amount to be withdrawn: "))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_draw = number_draw >= LIMIT_DRAW

        if exceeded_balance:
            print("Operation failed. You don't have enough balance!")
        elif exceeded_limit:
            print("Exceeded limit")
        elif exceeded_draw:
            print('Exceeded Draw')
        elif value > 0:
            balance -= value
            extract += f"Draw: $ {value: .2f}\n"
            number_draw += 1           
        else:
            print("Operation failed. Value not is valid")    

    elif option == '3':
        print ('\n========== Extract ==========')
        print("No account moves were made" if not extract else extract)
        print(f"\nBalance: ${balance: .2f}")
        print ('=============================')
    elif option == '4':
        break
    else:
        print('Invalid option')           