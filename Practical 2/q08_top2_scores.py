# Finding the two highest scores
# by Yiyang 29/01/18

studentNames = []
studentScores = []

index1 = 0     # initialising the 2 highest scores
index2 = 0
score1 = -1
score2 = -1

studentNo = int(input())

for i in range(studentNo):
    studentNames.append(input())
    studentScores.append(int(input()))
    
    if studentScores[i] > score1 :
        score2 = score1
        index2 = index1
        
        score1 = studentScores[i]
        index1 = i
    elif studentScores[i] > score2 :
        score2s = studentScores[i]
        index2 = i

print("The student with the highest score({1}) is {0},\nand the student with the second highest score({3}) is {2}.".format(studentNames[index1], score1, studentNames[index2], score2))