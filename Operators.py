name = raw_input("What is your name?")
age = input ("How old are you?")

bff = raw_input ("Who is your best friend?")
agebff= input("How old is your best friend?") 

if age == agebff:
    print name, "and", bff, "are the same age" 
    
elif age < agebff: 
    print name, "is younger than", namebff
    print name, "is", age, bff, "is", agebff
    
elif age > agebff:
    print name, "is older than", namebff
    print name, "is", age, bff, "is", agebff
