def user_choice():
    #Variables

    #initial 
    choice =  "wrong"
    acceptable_range = range(0,10)  
    within_range = False

    #Two conditions to check
    #Digit or within range == False

    while choice.isdigit() == False or within_range == False:
         choice = input("please enyer a number (0-10):")
       
         #Digit check
         if choice.isdigit() == False:
             print("sorry that is not a digit")

         if choice.isdigit() == True:
             if int(choice) in acceptable_range:
                 within_range = True
             else:
                 print("sorry you are out of range (0-10)")
                
         

    return int(choice)
    

print(user_choice())

 