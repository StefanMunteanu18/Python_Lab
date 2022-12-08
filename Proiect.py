import re
import collections
import sys


def is_cnp(string):
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

if __name__ == '__main__': 

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter path to text file *type '//' instead of '/'* : ")

    correct_path = False
    while correct_path == False:
        if(path.endswith(".txt")):
            try:
                f = open(path)
                correct_path = True
            except OSError:
                print("Could not open the specified file!")
        else:
            print("Incorrect path! The file needs to be a text file!")

        if correct_path == False:
            path = input("Enter path to text file *type '//' instead of '/'* : ")


    text = f.read()

    
    sentences_count = len(list(filter(lambda x: re.search('[a-zA-Z0-9]', x), re.split('[.|!|?]', text))))

    print("Propozitii : " + str(sentences_count))

    regex = re.compile('[^a-zA-Z0-9]')
    texy_no_punctuation = regex.sub(" ", text)
    print(texy_no_punctuation)
    words_count = len(texy_no_punctuation.split())
    print("Cuvinte : " + str(words_count))


    regex = re.compile('[^a-zA-Z]')
    text_letters_only = regex.sub("", text).lower()
    letters_count_total = len(text_letters_only)
    letters_count_dict = collections.Counter(text_letters_only)
    letters_list = sorted(list(letters_count_dict.keys()))
    for i in letters_list:
        print(i + " = " + str(letters_count_dict[i]) + " (" + str(letters_count_dict[i] / letters_count_total * 100) + "%" +")")

    phone_numbers = set(re.findall(" 07[0-9]{8} ", texy_no_punctuation))
    for i in phone_numbers:
        phone_numbers.remove(i)
        phone_numbers.add(i.strip())
    
    print("Numere telefon: " + str(len(phone_numbers)) + " " + str(phone_numbers))


    cnps = set(re.findall(" [0-9]{13} ", texy_no_punctuation))
    for i in cnps:
        cnps.remove(i)
        cnps.add(i.strip())
    cnps = list(filter(is_cnp, cnps))
    print("CNPuri: " + str(len(cnps)) + " " + str(cnps))
