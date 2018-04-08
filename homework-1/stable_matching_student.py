def main():

    professors =[]
    students=[]
    n = int(input())
    for i in range(n):
        professors.append([int(x) for x in input().split(' ')])
    for j in range(n):
        students.append([int(x) for x in input().split(' ')])
    print("Professor" , professors)
    print("Student",students)
    #free students
    free_student= []
    for i in range(len(students)):
        free_student.append(i)
    print("Free Student", free_student)

    partner_professor = [-1] * len(professors)
    partner_student = [-1] * len(students)

    while(len(free_student)>0):
        studentToBePaired = free_student.pop()
        print("Current Student ", studentToBePaired)
        for professor in students[studentToBePaired]:
            if partner_professor[studentToBePaired] == -1 and partner_student[professor] == -1:
                partner_professor[studentToBePaired] = professor
                partner_student[professor] = studentToBePaired
                print("Now Student ", studentToBePaired, "is paired with Professor ", professor)
                print("Student ", partner_student)
                print("Professor ", partner_professor)
                break
            else:
                currently_matched = partner_student[professor]
                print("Professor  ", professor, "is already paired with Student ", currently_matched)
                if (professors[professor].index(currently_matched) > professors[professor].index(studentToBePaired)):
                    partner_professor[currently_matched] = -1
                    partner_professor[studentToBePaired] = professor
                    partner_student[professor] = studentToBePaired
                    print("New Partner formed : Student ", studentToBePaired, 'is paired with Professor', professor)
                    print("Student ", partner_student)
                    print("Professor ", partner_professor)
                    free_student.append(currently_matched)
                    break

if __name__ == '__main__':
    main()