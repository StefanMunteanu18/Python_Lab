import math
import collections
import itertools

def is_prime(numar):

    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False

    max = int(math.sqrt(numar)) + 1

    for it in range(3, max + 1, 2):
      if numar % it == 0:
        return False
    
    return True

def ex1():
    n = int(input("enter n: "))
    results = []
    if n == 0:
        results.append(0)
    if n == 1:
        results.append(1)
    if n >= 2:
        results.append(0)
        results.append(1)
        for i in range(2, n + 1):
            results.append(results[i - 1] + results[i - 2])
    
    print(results)


def ex2(* numbers):
    solution = []
    for i in numbers:
        if is_prime(i):
            solution.append(i)
    print(solution)

def ex3(list_a, list_b):
    a_inters_b = []
    a_reunited_b = []
    a_minus_b = []
    b_minus_a = []
    for i in list_a:
        if i not in a_reunited_b:
            a_reunited_b.append(i)
        if i in list_b:
            a_inters_b.append(i)
        else:
            a_minus_b.append(i)
    for i in list_b:
        if i not in a_reunited_b:
            a_reunited_b.append(i)
        if i not in list_a:
            b_minus_a.append(i)
    print(a_inters_b)
    print(a_reunited_b)
    print(a_minus_b)
    print(b_minus_a)


def ex4(notes, moves, start):
    result = []
    result.append(notes[start])
    for i in moves:
        print(i, start)
        result.append(notes[(start + i) % len(notes)])
        start = (start + i) % len(notes)
    print(result)

def ex5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
                matrix[i][j] = 0
    for i in matrix:
        print(i)
    
def ex6(*lists, x):
    result = []
    for l in lists:
        for i in l:
            count = 0
            if i not in result:
                for k in lists:
                    count += k.count(i)
                if count == x:
                    result.append(i)

    print(result)

def ex7(numbers):
    count = 0
    greatest = -math.inf
    for i in numbers:
        if str(i) == str(i)[::-1]:
            count += 1
            if greatest < i:
                greatest = i

    result = (count, greatest)
    print(result)

def ex8(strings, x=2, flag=True):
    result = []
    for s in strings:
        l = []
        for c in s:
            if (ord(c) % x == 0) ^ (not flag):
                l.append(c)
        result.append(l)
    print(result)

def ex9(matrix):
    result = []
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    result.append((i,j))
                    break
    print(result)

def ex10(*lists):
    print(list(itertools.zip_longest(*lists)))

def ex11(l):
    print(sorted(l, key=lambda i: i[1][2]))

def ex12(words):
    rhymes = collections.defaultdict(list)
    for word in words:
        rhymes[word[-2:]].append(word)
    print(list(rhymes.values()))
    


if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            ex1()
        elif exercitiu == 2:
            ex2(1,2,3,4,5,6,7,8,9)
        elif exercitiu == 3:
            ex3([1,2,3,4,5], [4,5,6,7,8])
        elif exercitiu == 4:
            ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
        elif exercitiu == 5:
            ex5([[1,2,3,4,5], [4,5,6,7,8], [1,2,3,4,5], [4,5,6,7,8], [4,5,6,7,8]])
        elif exercitiu == 6:
            ex6([1,2, 3], [2,3,4],[4,5,6], [4,1, "test"], x = 2)
        elif exercitiu == 7:
            ex7([111,121,31,2211122])
        elif exercitiu == 8:
            ex8(["test", "hello", "lab002"], 2, False)
        elif exercitiu == 9:
            ex9([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]])
        elif exercitiu == 10:
            ex10([1,2,3], [5,6,7], ["a", "b", "c"])
        elif exercitiu == 11:
            ex11([('abc', 'bcd'), ('abc', 'zza')])
        elif exercitiu == 12:
            ex12(['ana', 'banana', 'carte', 'arme', 'parte'])
        else:
            break

