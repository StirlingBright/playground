if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input('Exam points:')
else:
    # hard-coded input for testing
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = 'exam_points1.csv'
with open(student_info) as new_file:
    student_info_dict = {}
    for line in new_file:
        line = line.replace('\n','')
        words = line.split(';')
        if words[0] == 'id':
            continue
        student_info_dict[words[0]] = [words[1],words[2]]


with open(exercise_data) as new_file:
    exercise_dict = {}
    exercise_points = {}
    for line in new_file:
        line = line.replace('\n','')
        words = line.split(';')
        if words[0] == 'id':
            continue
        exercise_dict[words[0]] = 0
        exercise_points[words[0]] = 0
        index = 0
        nums = words[1:]
        for word in nums:
            exercise_dict[words[0]] += int(nums[index])/4
            exercise_points[words[0]] += int(nums[index])
            index += 1
        exercise_dict[words[0]] = int(exercise_dict[words[0]])

with open(exam_data) as new_file:
    exam_dict = {}
    for line in new_file:
        line = line.replace('\n','')
        words = line.split(';')
        if words[0] == 'id':
            continue
        total = int(words[1]) + int(words[2]) + int(words[3])
        exam_dict[words[0]] = total


def convert_grades(num):
    if num >= 0 and num <= 14:
        return 0
    elif num >= 15 and num <= 17:
        return 1
    elif num >= 18 and num <= 20:
        return 2
    elif num >= 21 and num <= 23:
        return 3
    elif num >= 24 and num <= 27:
        return 4
    elif num >= 28:
        return 5


print(f'{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}')
for name in student_info_dict:
    print(f'{student_info_dict[name][0] + ' ' + student_info_dict[name][1]:<30}{exercise_points[name]:<10}{exercise_dict[name]:<10}{exam_dict[name]:<10}{exercise_dict[name] + exam_dict[name]:<10}{convert_grades(exercise_dict[name] + exam_dict[name]):<10}')

