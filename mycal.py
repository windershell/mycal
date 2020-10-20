#This is my first code for calculator using repeated-until loop, try-except, and elif condition
#by Winder
#trial calculator code


print ("Hello to mycal, you can try basic calculation for these 4 operation")

#This is the option of action to give to the user

print ("       ")

print ("1. try / again")
print ("2. exit")
answer = int(input("Enter option 1 or 2 :  "))

#This is the beginning of the repeated loop for the calculator action
while True:

    #This is the answer of the action option
    if (answer == 1):
        print ("       ")
        operation = input("Enter the option of operation (+ or - or * or /):")

        if (operation == '+'):
            #This is the condition that will inform user incase user didn't input number
            try:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                number3 = number1 + number2
                print(number3)
            except :
                print ("Please input number only")
        elif (operation == '-'):
                try :
                    number1 = int(input("Enter first number: "))
                    number2 = int(input("Enter second number: "))
                    number3 = number1 - number2
                    print(number3)
                except :
                    print ("Please input number only")
        elif (operation == '*'):
            try:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                number3 = number1 * number2
                print(number3)
            except :
                print ("Please input number only")
        elif (operation == '/'):
            try:
                number1 = int(input("Enter first number: "))
                number2 = int(input("Enter second number: "))
                #This is math rule that number can't be divided by 0 / zero
                if (number2 == 0):
                    print ("cannot divide by 0")
                else :
                    number3 = number1 / number2
                    print(number3)
            except :
                print ("Please input number only")
        #This is the break when the user want to exit calculator
        elif (operation == 'exit'):
            break
        else :
            print ("Operation is not recognized, try again and input operation  + or - or * or /")

        #This mesage to inform user how to break the loop
        print ("       ")
        print ("type exit for exit")

    elif (answer == 2):
        print ("Ok, See ya")
        break

    #This is to inform user action option only 1 and 2 and stop the calculator
    else :
        print ("Please input 1 or 2 only")
        break
