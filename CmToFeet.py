def cmToFeetConverter():
    userGuess = input("Guess your height in feets! ")                    
    userInput = input("Enter your height in cm: ")
    resultInFeet = round(float(userInput) / 30.48 , 1)
    #print(str(resultInFeet))
    if round(float(userGuess),1) == resultInFeet:
       print("Wow! You've guessed it right!")
    else: 
      print("It's okay! Try Again!")

cmToFeetConverter()
