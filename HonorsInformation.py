"""
File: HonorsInformation.py
Author: Michael Riesberg-Timmer
Description: Process all avaialable lists of UNI Dean's List students and extract
            information
"""
import os

fileList = os.listdir(os.getcwd())
masterDict = dict()

for eachFile in fileList:
    if eachFile != "HonorsInformation.py":
        fin = open(eachFile,"r")
        for line in fin:
            if line == '\n' or line == '':
                pass
            else:
                line = line.split()
                
                #format student names into first and last name format
                #Does not account for students with same first and last name
                if len(line) == 3:
                    student = line[0] + " " + line[2]
                elif len(line) == 2:
                    student = line[0] + " " + line[1]
                    
                    
                
                if student in masterDict:
                    masterDict[student].add(eachFile[:-4])
                else:
                    masterDict[student]=set()
                    masterDict[student].add(eachFile[:-4])
    else:
        pass

totalStudents = 0.0
oneSemester = 0.0
twoSemesters = 0.0
threeSemesters = 0.0
fourSemesters = 0.0
fiveSemesters = 0.0
sixSemesters = 0.0
sevenSemesters = 0.0
eightSemesters = 0.0
for student in masterDict:
    totalStudents += 1
    if len(masterDict[student]) == 1:
        oneSemester += 1
    elif len(masterDict[student]) == 2:
        twoSemesters += 1
    elif len(masterDict[student]) == 3:
        threeSemesters += 1
    elif len(masterDict[student]) == 4:
        fourSemesters += 1
    elif len(masterDict[student]) == 5:
        fiveSemesters += 1
    elif len(masterDict[student]) == 6:
        sixSemesters += 1
    elif len(masterDict[student]) == 7:
        sevenSemesters += 1
    elif len(masterDict[student]) == 8:
        eightSemesters += 1



print("The following lines are the number of semesters a student was on the Dean's List and the percentage of all Dean's List students to be on the Dean's List that many times\n")
print("A total of " + str(totalStudents) + " students have been on the honor roll between the Fall of 2012 and the spring of 2016")
print("One Semester - " + str((oneSemester*100)/totalStudents) + "% of students")
print("Two Semesters - " + str((twoSemesters*100)/totalStudents) + "% of students")
print("Three Semesters - " + str((threeSemesters*100)/totalStudents) + "% of students")
print("Four Semesters - " + str((fourSemesters*100)/totalStudents) + "% of students")
print("Five Semesters - " + str((fiveSemesters*100)/totalStudents) + "% of students")
print("Six Semesters - " + str((sixSemesters*100)/totalStudents) + "% of students")
print("Seven Semesters - " + str((sevenSemesters*100)/totalStudents) + "% of students")
print("Eight Semesters - " + str((eightSemesters*100)/totalStudents) + "% of students")
print(" ")

#stop program from exiting immediately
input("Press Enter to Exit")

























