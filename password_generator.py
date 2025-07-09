import random
import string

def generate_strong_password(length: int, nums: bool, punctuation: bool):
    special = '!?=+-()#'
    output = ''
    if nums == False and punctuation == False:
        for number in range(length):
            output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()

    elif nums == True and punctuation == False:
        while len(output) < length:
            if len(output) == length - 2:
                check = True
                for letter in output:
                    if letter.isdigit():
                        check = False
                        continue
                if check == True:
                    output += str(random.randint(0,9))
            if len(output) == length - 1:
                check = True
                for letter in output:
                    if letter.isalpha():
                        check = False
                        continue
                if check == True:
                    output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
            choice = random.randint(0,1)
            if choice == 0:
                output += str(random.randint(0,9))
            else:
                output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
    elif nums == False and punctuation == True:
        while len(output) < length:
            if len(output) == length - 2:
                check = True
                for letter in output:
                    if letter.isdigit():
                        check = False
                        continue
                if check == True:
                    output += special[random.randint(0,len(special)-1)]
            if len(output) == length - 1:
                check = True
                for letter in output:
                    if letter.isalpha():
                        check = False
                        continue
                if check == True:
                    output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
            choice = random.randint(0,1)
            if choice == 0:
                output += special[random.randint(0,len(special)-1)]
            else:
                output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
    elif nums == True and punctuation == True:
        while len(output) < length:
            if len(output) == length - 3:
                check = True
                for letter in output:
                    if letter.isdigit():
                        check = False
                        continue
                if check == True:
                    output += str(random.randint(0,9))
            if len(output) == length - 2:
                check = True
                for letter in output:
                    if letter.isalpha():
                        check = False
                        continue
                if check == True:
                    output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
            if len(output) == length - 1:
                check = True
                for letter in output:
                    if letter in special:
                        check = False
                        continue
                if check == True:
                    output += special[random.randint(0,len(special)-1)]
            choice = random.randint(0,2)
            if choice == 0:
                output += str(random.randint(0,9))
            elif choice == 1:
                output += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)].lower()
            elif choice == 2:
                output += special[random.randint(0,len(special)-1)]
    return output[:length]


if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(12, True, False))
