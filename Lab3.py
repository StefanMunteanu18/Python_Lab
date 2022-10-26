import itertools

def ex1(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    result = []
    result.append(set_a.union(set_b))
    result.append(set_a.intersection(set_b))
    result.append(set_a.difference(set_b))
    result.append(set_b.difference(set_a))
    print(result)

def ex2(string):
    letters_set = set(string)
    result = dict()
    for i in letters_set:
        result[i] = string.count(i)
    print(result)

def ex3(dict_a, dict_b):
    if dict_a.keys() != dict_b.keys():
        print("False")
        return False
    for key in dict_a.keys():
        if type(dict_a[key]) == type(dict_b[key]):
            if type(dict_a[key]) == dict and type(dict_b[key]) == dict:
                ex3(dict_a[key], dict_b[key])
            else:
                if dict_a[key] != dict_b[key]:
                    print("False")
                    return False
        else:
            print("False")
            return False
    print("True")
    return True

def ex4(tag, content, **args):
    result = "<" + tag + " "
    for key in args.keys():
        result += str(key) + r'=\"' + args[key] + r'\"'
    result += ">" + content + r'</' + tag + ">"
    print(result)


def ex5(rules, dictionary):
    rules_dict = dict((x, (p, m, s)) for x, p, m, s in rules)
    for key in dictionary.keys():
        if key not in rules_dict.keys():
            print("False1")
            return False
        if not dictionary[key].startswith(rules_dict[key][0]):
            print("False2")
            return False
        if not dictionary[key].endswith(rules_dict[key][2]):
            print("False3")
            return False
        if rules_dict[key][1] not in dictionary[key][1:-1]:
            print("False4")
            return False
    print("True")
    return True
    #for tpl in rules:
        
def ex6(numbers):
    numbers_set = set(numbers)
    a = len(numbers_set)
    b = 0
    for i in numbers_set:
        if numbers.count(i) >= 2:
            b += 1
    print((a, b))
    
def ex7(*sets):
    result = {}
    for a, b in itertools.combinations(sets, 2):
        result[str(a) + " | " + str(b)] = a.union(b)
        result[str(a) + " & " + str(b)] = a.intersection(b)
        result[str(a) + " - " + str(b)] = a.difference(b)
        result[str(b) + " - " + str(a)] = b.difference(a)
    print(result)

def ex8(dictionary):
    result = []
    key = "start"
    val = dictionary[key]
    while val not in result:
        result.append(val)
        key = val
        val = dictionary[key]
    print(result)

def ex9(*args1,**args2):
    result = 0
    for pos in args1:
        if pos in args2.values():
            result += 1
    print(result)


if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            ex1([1,2,3,4,5], [4,5,6,7,8])
        elif exercitiu == 2:
            ex2("ana are mere")
        elif exercitiu == 3:
            ex3({"A":[1,2], "B":2}, {"A":[1,2], "B":2})
        elif exercitiu == 4:
            ex4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
        elif exercitiu == 5:
            ex5({("key1", "co", "inside", "zz"), ("key2", "th", "not", "id")}, {"key1": "come inside, it's too cold out", "key2": "this is not valid"})
        elif exercitiu == 6:
            ex6([1,1,1,4,2,3,1,3,4,5])
        elif exercitiu == 7:
            ex7({1,2}, {2, 3}, {3, 4})
        elif exercitiu == 8:
            ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
        elif exercitiu == 9:
            ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5)
        else:
            break
