def ex2(*args, **kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum

ex2_lam = lambda *args, **kwargs : sum(kwargs.values())

def ex3_1(inp):
    result = []
    for ltr in inp:
        if ltr in "aeiouAEIOU":
            result.append(ltr)
    return result

def ex3_2(inp):
    return list(filter(lambda x : x in "aeiouAEIOU", inp))

def ex3_3(inp):
    return[letter for letter in inp if letter in "aeiouAEIOU"]

def ex4(*args, **kwargs):
    args = list(args)
    args.extend(kwargs.values())
    dictionaries = (list(filter(lambda x : isinstance(x, dict), args)))
    dictionaries_2keys = (list(filter(lambda x : len(x.keys()) >= 2, dictionaries)))
    result = (list(filter(lambda x : max([len(str(k)) for k in x.keys()]) >= 3, dictionaries_2keys)))

    return result

def ex5(inp_list):  
    restult = list(filter(lambda x : isinstance(x, (int, float)), inp_list))
    return restult

def ex6(inp_list):
    even = list(filter(lambda x : x % 2 == 0, inp_list))
    odd = list(filter(lambda x : x % 2 == 1, inp_list))
    print(even)
    print(odd)
    result = list(zip(even, odd))
    return result

def sum_digits(x):

    return sum(map(int, str(x)))

def ex7(**kwargs):
    fib = [0, 1]
    n1 = 0
    n2 = 1
    for i in range(998):
        aux = n1 + n2
        fib.append(aux)
        n1 = n2
        n2 = aux

    if("filters" in kwargs.keys()):
        for predicate in kwargs["filters"]:
            fib = list(filter (predicate, fib))

    if("offset" in kwargs.keys()):
        fib = fib[kwargs["offset"]:]

    if("limit" in kwargs.keys()):
        fib = fib[: kwargs["limit"]]
    return fib
    
#def ex8():

def ex9(pairs):
    result = []
    for pair in pairs:
        dictionary = dict()
        dictionary["sum"] = pair[0] + pair[1]
        dictionary["prod"] = pair[0] * pair[1]
        dictionary["pow"] = pair[0] ** pair[1]
        result.append(dictionary)
    return result


#print(ex2(1, 2, 3, a=2, b=7))
#print(ex2_lam(1,2, a=3, b=-2))
#print(ex3_3("qotheowqifmwlqfrqiyaaaoiq"))
#print(ex4( {1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
#print (ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
#print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
#print(ex7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))
print(ex9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))