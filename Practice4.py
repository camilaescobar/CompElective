sub1 = raw_input("What is your favorite subject?")
grade = input ("What is your grade?")

sub2 = raw_input ("What is your second favorite subject?")
grade2= input("What is your grade") 

if grade == grade2:
    print sub1, "and", sub2, "are Camila's favorite subjects" 
    
elif grade < grade2: 
    print "Camila has a higher grade in",sub2, "than in", sub1
    print sub1, "is", grade, sub2, "is", grade2
    
elif grade > grade2:
    print "Camila has a higher grade in", sub1, "than in", sub2
    print sub1, "is", grade, sub2, "is", grade2

gpa = ((sub1 * 4.3)+(sub2 *4.3)) / 2 

print "Camila's GPA is", gpa
