'''import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)
logarithm = math.log10(5)
print(logarithm)
sine = math.sin(90)
print(sine)'''

'''import random

value = random.randint(1, 6)
print(value)'''


'''import math

def triangle_area(a, b, c):
    try:
        smallp = (a+b+c)/2
        return math.sqrt(smallp*(smallp-a)*(smallp-b)*(smallp-c))
    except:
        print("Error ocurred! Oopsie...")
        return str("nothing! Error ocurred.")

a = int(input('Enter A'))
b = int(input('Enter B'))
c = int(input('Enter C'))

print(f"The area of ​​a triangle with sides {a, b, c} is {triangle_area(a, b, c)}")'''


'''def sum_digits(number):
    aboslut = str(abs(number))
    sum = 0
    for i in range(len(aboslut)):
        sum = sum + int(aboslut[i])
    return sum
    

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the numbers is', result)'''

##
# Calculates the final grade for a test based
# on the number of points obtained
#
'''def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 18
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}!')'''


def time_string(hours, minutes, time_format):
    result = ''
    # hours
    if time_format == 24:
        if len(str(hours)) == 1:
            result += '0' + str(hours)
        else:
            result = result + str(hours)
    elif time_format == 12:
        if len(str(hours)) == 1:
            result = result + '0' + str(hours) + 'am'
        else:
            if hours >= 13:
                hours -= 12
                if hours < 10
            result = result + str(hours) + 'pm'
    else:
        result = 'You wrote wrong time format!'
    result += ':'
    # minutes
    if len(str(minutes)) == 1:
        result += '0' + str(minutes)
    else:
        result = result + str(minutes)
        
    return result


