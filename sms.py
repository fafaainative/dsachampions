#Student Result Management Helper

# A simple Student Result Helper that can
# calculate a student's average score;
# determine whether the student passed or failed;
# assign a grade based on the average score;
# generate a readable student result summary.

 #First create a dictionary to store student info. 

students = [
    {
    "name" : "Ada",
    "mathematics" : 70,
    "english" : 80,
    "biology" : 90
},

{
    "name" : "John",
    "mathematics" : 60,
    "english" : 65,
    "biology" : 75
}
]

def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3)/3
    return average


def result_status(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    
def assign_grade(average):
    if average < 0 and average >100:
        return "Wrong average"
    if average >= 70:
        return  "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return  "C"
    elif average >= 40:
        return  "D"
    else:
        return "F"
def result_summary(name, average, grade, status):
    
    print("=" * 10, " STUDENT RESULT ", "=" * 10 )
    print("- " * 20)

    




