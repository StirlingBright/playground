from datetime import datetime
from datetime import timedelta

if False:
    filename = 'late_june.txt'
    starting_date = '24.6.2020'
    date = datetime.strptime(starting_date, "%d.%m.%Y")
    length = 2
else:
    filename = input('Filename:')
    starting_date = input('Starting date:')
    date = datetime.strptime(starting_date, "%d.%m.%Y")
    starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
    length = int(input('How many days:'))

print('Please type in screen time in minutes on each day (TV computer mobile):')
one_day = timedelta(days=1)
total = 0
new_line = []
for num in range(length):
    time = input(f'{date.day}.{date.month}.{date.year}:')
    numbers = time.split(' ')
    for number in numbers:
        total += int(number)
        new_line.append(number + '/')
    new_line[-1] = new_line[-1][:-1]
    date += one_day
with open(filename, 'w') as new_file:
    date -= one_day
    new_file.write(f'Time period: {starting_date.strftime("%d.%m.%Y")}-{date.strftime("%d.%m.%Y")}\n')
    new_file.write(f'Total minutes: {total}\n')
    new_file.write(f'Average minutes: {total/length}\n')
    index2 = 0
    for num in range(length):
        new_file.write(f'{starting_date.strftime("%d.%m.%Y")}: {new_line[index2]}{new_line[index2+1]}{new_line[index2+2]}\n')
        starting_date += one_day
        index2 += 3
print(f'Data stored in {filename}')
#print(new_line)
