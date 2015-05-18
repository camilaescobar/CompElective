#Name
#LastName
#ComputerClass
#YOB
#calculate age, 
#Calculate S1
#S2
#Final grde

name = raw_input("What is your name?")
LastName = raw_input("What is your last name?")
subject = raw_input ("What class are you in?")
yob= input("What year were you born in?") 
age= 2015 - yob 
semester1 = input ("What grade did you have in semester 1?") 
semester2 = input ("What grade did you have semester 2?") 
final = (semester1 + semester2) / 2 

print  name, LastName, "you are", age, "years old"
print "your average for", subject, "is", final 
