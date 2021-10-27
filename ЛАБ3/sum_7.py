op=int(input())
math_analysis=int(input())      
discrete_mathematics=int(input())
creative_approach=int(input())
history=int(input())
percent_grade=float((op+math_analysis+discrete_mathematics+creative_approach+history)/5)
round(percent_grade,2)
letter_grade=int()
if percent_grade<0 or percent_grade>100:
    print("None")
elif op>100 or op<0:
    print("None")
elif math_analysis>100 or math_analysis<0:
    print("None")
elif discrete_mathematics>100 or discrete_mathematics<0:
    print("None")
elif creative_approach>100 or creative_approach<0:
    print("None")
elif history>100 or history<0:
    print("None")
elif percent_grade==0:
    print("Average grade = 0 -> F")
elif percent_grade<=60:
    letter_grade=="F"
    print("Average grade =",percent_grade,"-> F")
elif percent_grade<=67:
    letter_grade=="E"
    print("Average grade =",percent_grade,"-> E")
elif percent_grade<=75:
    letter_grade=="D"
    print("Average grade =",percent_grade,"-> D")
elif percent_grade<=82:
    print("Average grade =",percent_grade,"-> C")
elif percent_grade<=90:
    letter_grade="B"
    print("Average grade =",percent_grade,"-> B")
elif percent_grade<=100:
    letter_grade="A"
    print("Average grade =",percent_grade,"-> A")
