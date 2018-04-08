"""
CSCI-665-01 Homework-1-3(match.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input from user and find stable matching by first matching
professor with students and viceversa.Matching by professor and student are
compared for same match in both cases. The number of such matches is printed
as output.

Usage: python3 match.py
number
professor preference
student preference

"""

'''
The main function takes student and professor preference and start matching
professor and then start matching students. The output of the above results
is compared to find same pairs formed while first pairing professor to students
and then pairing students with professor
'''
def main():
    # store professor preference
    professors = []
    #store student preference
    students = []
    #number of students and professor
    n = int(input())
    #take preference of professor
    #complexity - n
    for i in range(n):
        professors.append([int(x) for x in input().split(' ')])
    #take prefernce of student
    # complexity - n
    for j in range(n):
        students.append([int(x) for x in input().split(' ')])
    #start stable matching for pairing students
    # complexity - n^2
    result_professor = stableMatchProfessor(professors,students)
    #start stable matching for pairing professor
    # complexity - n^2
    result_student = stableMatchStudent(professors,students)

    #valid match
    valid_match = 0
    # complexity - n
    i , j = 0, 0
    #to calculate same pairs forms
    while(i<len(result_professor) and j < len(result_student)):
        if result_professor[i] == result_student[j]:
            valid_match+=1
        i+=1
        j+=1
    print(valid_match)

'''
The function gives the pairing of professor and students
according to professor.

@:param : professor preference
@:param : student preference

@:return : pairs professor and student

Complexity :  O(n^2)

'''

def stableMatchProfessor(professors,students):
    # to store free professor
    free_professor = []
    # assign free professors
    for i in range(len(professors)):
        free_professor.append(i)

    # maintain for matching

    partner_professor = [-1] * len(professors)
    partner_student = [-1] * len(students)

    '''
    
    The loop works as follows:
    1. Check if there are any free professor
    2. If yes, pop a free professor from list of free professor 
    3. Check the preference of professor and check if student is free
    4. If student is free the pair professor and student
    5. Else check the preference of student for the current professor and
    new professor if new professor has more preference then it is matched with
    new professor and current professor is added to free professor else it goes
    to next student 
    6. Loop continues until all the professor are matched with students
    
    '''
    while (len(free_professor) > 0):
        #pop professor to be paired
        professorToBePaired = free_professor.pop()
        #iterate his preference
        for student in professors[professorToBePaired]:
            #if student free then pair professor with student
            if partner_student[professorToBePaired] == -1 and\
                            partner_professor[student] == -1:
                partner_student[professorToBePaired] = student
                partner_professor[student] = professorToBePaired
                break
            else:
                #get the current match of student
                currently_matched = partner_professor[student]
                #compare the preference if current match has lower preference
                #assign new professor to the student and free current professor
                if (students[student].index(currently_matched) >
                        students[student].index(professorToBePaired)):
                    partner_student[currently_matched] = -1
                    partner_student[professorToBePaired] = student
                    partner_professor[student] = professorToBePaired
                    free_professor.append(currently_matched)
                    break
    return partner_student

'''
The function gives the pairing of professor and students
according to student.

@:param : professor preference
@:param : student preference

@:return : pairs professor and student

Complexity : O(n^2)
'''

def stableMatchStudent(professors,students):
    #to track free students
    free_student = []
    #assign free students
    for i in range(len(students)):
        free_student.append(i)
    #to store the match
    partner_professor = [-1] * len(professors)
    partner_student = [-1] * len(students)
    '''

        The loop works as follows:
        1. Check if there are any free student
        2. If yes, pop a free student from list of free student 
        3. Check the preference of student and check if professor is free
        4. If professor is free then pair professor and student
        5. Else check the preference of professor for the current student and
        new student if new student has more preference then it is matched with
        new student and current student is added to free student else it goes 
        to next professor 
        6. Loop continues until all the students are matched with professor.

        '''
    while (len(free_student) > 0):
        #pop free student
        studentToBePaired = free_student.pop()
        #iterate student  preference
        for professor in students[studentToBePaired]:
            #check if student free if yes pair them
            if partner_professor[studentToBePaired] == -1 and \
                            partner_student[professor] == -1:
                partner_professor[studentToBePaired] = professor
                partner_student[professor] = studentToBePaired
                break
            else:
                #get his current professor
                currently_matched = partner_student[professor]
                #compare preference if current match has lower preference
                #assign new student to professor and free current student
                if (professors[professor].index(currently_matched) >
                        professors[professor].index(studentToBePaired)):
                    partner_professor[currently_matched] = -1
                    partner_professor[studentToBePaired] = professor
                    partner_student[professor] = studentToBePaired
                    free_student.append(currently_matched)
                    break
    return partner_student



if __name__ == '__main__':
    main()