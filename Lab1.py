import math
import collections

def ex1(* numbers):
    if len(numbers) == 2:
        gcd = math.gcd(numbers[0], numbers[1])
        print(gcd)
    elif len(numbers) >= 2:
        gcd = math.gcd(numbers[0], numbers[1])
        for index in range(2, len(numbers)):
            gcd = math.gcd(gcd, numbers[index])
        print(gcd)
    else :
        print("Not enought numbers!")


def ex2():
    string = input("enter string: ")
    print(string)
    vow_count = 0
    for letter in string:
        if letter in "aeiouAEIOU":
            vow_count += 1
    print (vow_count)

def ex3():
    f_string = input("enter first string: ")
    s_string = input("enter second string: ")
    print(s_string.count(f_string))

def ex4():
    string = input("enter string: ")
    for letter in string:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            low_letter = letter.lower()
            string = string.replace(letter, "_"+low_letter)
    print(string)

def ex5():
    n = int(input("enter dimension: "))
    matrix = []
    row = []
    print("enter matrix elements: ")
    for i in range (0, n):
        for j in range (0, n):
            row.append(input())
        matrix.append(row)
        row = []

    print(matrix)

    while len(matrix) > 0:
        if len(matrix) > 0:
            for col in matrix[0]:
                print(col)
            matrix.pop(0)

        if len(matrix) > 0:
            for row in matrix:
                print(row[-1])
                row.pop(-1)

        if len(matrix) > 0:
            for col in reversed(matrix[-1]):
                print(col)
            matrix.pop(-1)

        if len(matrix) > 0:
            for row in reversed(matrix):
                print(row[0])
                row.pop(0)
    
def ex6():
    string = input("enter number: ")
    string_reversed = string[::-1]
    if(string == string_reversed):
        print("palindrome!")
    else:
        print("not palindrome!")

def ex7():
    string = input("enter text: ")
    number_found = False
    number = "no number found!"
    for i in string:
        if i in "0123456789":
            if number_found == False:
                number_found = True
                number = i
            else:
                number += i
        elif number_found == True:
            break

    print(number)         

def ex8():
    n = int(input("enter bumber: "))
    print (bin(n))
    print (bin(n).count("1"))

def ex9():
    string = input("enter string: ")
    coutner = collections.Counter(string)
    print(coutner.most_common(1))

def ex10():
    string = input("enter string: ")
    print(string.split())
    

if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            ex1()
        elif exercitiu == 2:
            ex2()
        elif exercitiu == 3:
            ex3()
        elif exercitiu == 4:
            ex4()
        elif exercitiu == 5:
            ex5()
        elif exercitiu == 6:
            ex6()
        elif exercitiu == 7:
            ex7()
        elif exercitiu == 8:
            ex8()
        elif exercitiu == 9:
            ex9()
        elif exercitiu == 10:
            ex10()
        else:
            break

