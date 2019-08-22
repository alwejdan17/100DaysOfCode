

GPA=["Excellent","Very Good","Good"]
Scores=[95,85,65]


for Score in Scores:
    if Score>=90:
        print("Score =",str(Score),"and The type of Score is ",str(type(Score)),"\nGPA =" ,str(GPA[0])," and the Type of GPA is",str(type(GPA[0])))
    elif Score>=80:
        print("Score =",str(Score),"and The type of Score is ",str(type(Score)),"\nGPA =" ,str(GPA[1])," and the Type of GPA is",str(type(GPA[1])))
    else:
        print("Score =",str(Score),"and The type of Score is ",str(type(Score)),"\nGPA =" ,str(GPA[2])," and the Type of GPA is",str(type(GPA[2])))

