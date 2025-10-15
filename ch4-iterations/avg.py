#sum of scores that are above average
scores=[80,60,50,65,75,55]
def sum(scores):
    totalSum=0
    totalStudents=0
    for i in scores:
        totalSum+=i
        totalStudents+=1
    avg=totalSum/totalStudents
    sum=0
    for i in scores:
        if i>avg:
            sum+=i
    return sum
print(sum(scores))