def distribute(students,apples):
    each = apples//students
    remain = apples%students
    print('Each student will take '+str(each)+' apples, and remains '+str(remain))
distribute(6,31)
