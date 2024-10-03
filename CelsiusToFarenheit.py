
# feh = (celsius * 9/5) + 32
#Enter a temperature in degrees Celsius: 23.4
#23.4 degrees celsius are 74.12 degrees Farenheit.
def converter():
        
           celsius = input("Enter a temperature in degrees Celsius: ")
           floatCel = float(celsius)
           if  floatCel >= -89.2 and floatCel <= 56.7:
              feh = (floatCel * 9/5) + 32
              print(celsius + " degrees Celsius are " + 
                 str(feh) + " degrees Farenheit.")
           else:
              print("Enter a valid Celsius degree.") 

converter()