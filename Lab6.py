import re
import os

def ex1(text):
    r = re.compile("^\w+$")
    words = list(filter(lambda x: r.match(x), text.split(" ")))
    return words

def ex2(reg, text, num):
    r = re.compile(reg)
    result = []
    if num == 0:
        return []
    else:
        for i in range(len(text) - num + 1):
            substr = text[i : i + num]
            if r.match(substr):
                result.append(substr)
    return result

def ex3(text, regs):
    regs_compiled = []
    result = set()

    for i in regs:
        result |= set(re.findall(i, text))

    return result

def ex4(path, attrs):
    f = open(path)
    string = f.read()

def censor(matchobj):
    word_list = list(matchobj.group(0))
    beggining_space = False
    ending_space = False
    print(word_list)
    if word_list[0] == " ":
        beggining_space = True
        word_list.pop(0)
    if word_list[-1] == " ":
        ending_space = True
        word_list.pop(-1)

    for i in range(len(word_list)):
        if i % 2 == 1:
            word_list[i] = "*"
    
    if beggining_space:
        word_list.insert(0, " ")
    if ending_space:
        word_list.append(" ")
    print(word_list)


    return "".join(word_list)

def ex6(text):
    result = re.sub("(^|\s)[aeiouAEIOU]\w*[aeiouAEIOU]($|\s)", censor, text)
    return result

def ex7(string):

    r = re.compile("[12345678][0-9][0-9]([0][1-9]|10|11|12)([0-2][0-9]|30|31)([0-4][0-9]|51|52)[0-9][0-9][0-9][0-9]")
    if not r.match(string):
        return False

    digits = list(string)
    month = int(digits[3]+digits[4])
    day = int(digits[5]+digits[6])
    if (month <= 7 and month % 2 != 1) or (month > 7 and month % 2 != 0):
        if day == 31:
            return False

    if month == 2 and day > 29:
        return False
    else:
        year = 1900
        if digits[0] == "1" or digits[0] == "2" or digits[0] == "7" or digits[0] == "8":
            year = 1900
        if digits[0] == "3" or digits[0] == "4":
            year = 1800
        if digits[0] == "5" or digits[0] == "6":
            year = 2000
        year += int(digits[1]+digits[2])
        if not((year % 4 == 0 and year % 100 !=0) or year % 400 == 0):
            if day > 28:
                return False

    county = int(digits[7]+digits[8])
    if county == 49:
        return False

    if digits[9] == "0" and digits[10] == "0" and digits[11] == "0":
        return False

    const = list("279146358279")
    sum = 0
    for i in range(12):
        sum += int(digits[i]) * int(const[i])
    if sum % 11 < 10:
        c = sum % 11
    else:
        c = 1

    if digits[12] != str(c):
        return False

    return True

def ex8(path, reg):
    r = re.compile(reg)
    for root, dirs, files in os.walk(path):
        for name in files:
            fullname = os.path.join(root, name)
            if r.match(fullname):
                print(fullname)
        for name in dirs:
            fullname = os.path.join(root, name)
            if r.match(fullname):
                print(fullname)

if __name__ == '__main__': 
    #print(ex1("sdad afaasfaf   r4334dsfaff afasdsad ,fafa, afsadaa"))
    #print(ex2("^\w+$", "125.1r..,f1.w,f1g,.1,sdqgg.,", 3))
    #print(ex3("1232 dwqewq 23a fdasfs.. fa .../ 2", ["\d+", "\w+"]))
    #ex4("D:\\Desktop\\xmlfile.xml", 2)
    #print(ex6("adssdse dsadad areetefdfaoo"))
    #print(ex7("6120517016371"))
    print(ex8("D:\\Desktop",".*Photoshop.*"))