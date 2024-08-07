## interactive Calculator
### Give Choice to User


print ("\n\t\t\tWhat Function You want To Use")
Choice = 0
while Choice <8:
    
    Choice = int (input("\n\t 1. Summation \t 2. Difference \t 3. Multiplication \t 4. Division \n\n\t 5. Power of \t 6. Remainder \t 7. Floor Division \t 8. Exit\n\n\t"))

    if Choice <8:
        first_number = int (input("\n\t\tProvide First Number\n\t"))
        second_number = int (input("\n\t\tProvide Second Number\n\t"))

        if Choice == 1:

            ### Performing the Funtion 

            print ("\n\t\t The Sum Of Two Number Is: \n\t\t", first_number + second_number)
            print ("\n\t\t What Else You Want To Do ! Master\n")

        elif Choice == 2:

            ### Performing the Funtion 

            print ("\n\t\t The Difference is: \n\t\t", first_number - second_number)
            print ("\n\t\t Your Wish Is My Command\n")

        elif Choice == 3:

            ### Performing the Funtion 

            print ("\n\t\t The Multiple Of Two Number Is: \n\t\t", first_number * second_number)
            print ("\n\t\t You can't Even Do that Sire\n")

        elif Choice == 4:
        
            ### Performing the Funtion 

            print ("\n\t\t The Division Of Two Number Is: \n\t\t", first_number / second_number)
            print ("\n\t\t What Ever you say My Lord\n")

        elif Choice == 5:

            ### Performing the Funtion 

            print ("\n\t\t The Answer Is: \n\t\t", first_number ** second_number)
            print ("\n\t\t I have Given Power to your Integer, what Else ?\n")

        elif Choice == 6:
        
            ### Performing the Funtion 

            print ("\n\t\t The Remainder is: \n\t\t", first_number % second_number)
            print ("\n\t\t Hmm, Lets Try Another one. Since you  don't Know this simple Math\n")

        elif Choice == 7:

        ### Performing the Funtion 

            print ("\n\t\t The Floor Number Is: \n\t\t", first_number // second_number)
            print ("\n\t\t Is that All Master ?\n")
    
        else:
            break
    else:
        break
else: 
    ()