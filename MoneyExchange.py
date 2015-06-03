#value of number in dollars, euros, yens
#ask to input number
#ask to input currency
#show exchange 

value = input("Please enter the value in numbers:") 
currency = raw_input("Please enter your currency:")

if currency == "dollars":
   euros = money = 0.92
   yens = money = 124.35
   print "your $", money, "are: €", euros, "and ¥", yens 
   
elif currency == "euros": 
    dollars = money * 0.92
    yens = money * 124.35
    print "your €", money, "are: $", dollars, "and ¥:", yens 
    
elif currency == "yens": 
    dollars= money = 0.0081
    euros= money * 0.0074
    print "your ¥", money, "are: $", dollars, "and €", euros 
    
else: 
    print "Select the correct currency, please try again"
    
