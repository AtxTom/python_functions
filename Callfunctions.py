
def Pay(Hours,Rate,EligibleForOvertime):
      if (Hours > 40) and EligibleForOvertime:
            return 40*Rate + (Hours-40)*Rate*1.5
      else:
            return Hours*Rate
      
Dollars = Pay(50.0,7.25,True)
print ('You earned $' ,Dollars)


# Alternative 
#    
def main():
      # Set a variable to the the Pay function and pass the arguements.
      Dollars = Pay(50.0,7.25,True)
      print ('You earned $' ,Dollars)
      
      # Alternatively you can add the function call to a print statment

      print ('You earned $' ,Pay(50.0,7.25,True))

def Pay(Hours,Rate,EligibleForOvertime):
    if (Hours > 40) and EligibleForOvertime:
      return 40*Rate + (Hours-40)*Rate*1.5
    return Hours*Rate

# Call the main function.
main()
