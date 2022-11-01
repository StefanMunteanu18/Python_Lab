import os
import sys

def ex1(dir_path):
    content_list = os.listdir(dir_path)
    extensions = set()
    for fl_name in content_list:
        if os.path.isdir(os.path.join(dir_path, fl_name)) == False:
            extensions.add(fl_name.split(".")[-1])
    sorted_list = sorted(extensions)
    print(sorted_list)
    return sorted_list

def ex2(dir_path, file_path):
    f = open(file_path, "w")
    content_list = os.listdir(dir_path)
    for fl_name in content_list:
        if os.path.isdir(os.path.join(dir_path, fl_name)) == False and (fl_name[0] == "A" or fl_name[0] == "a") :
            f.write(os.path.join(dir_path, fl_name) + '\n')

def ex3(path):
    if os.path.isdir(path):
        ext_count_dict = {}
        for (root,directories,files) in os.walk(path):
            for fileName in files:
                if "." in fileName:
                    ext = fileName.split(".")[-1]
                    ext_count_dict[ext] = ext_count_dict.get(ext, 0) + 1
        ext_count_list = [(k, v) for k, v in ext_count_dict.items()]
        print(ext_count_list)
        return ext_count_list
    elif os.path.isfile(path):
        f = open(path, "r")
        result = f.read()[-20:]
        print(result)
        return result
    else:
        print("Incorrect path!")
        return -1

def ex4():
    content_list = os.listdir(sys.argv[1])
    extensions = set()
    for fl_name in content_list:
        if os.path.isdir(os.path.join(sys.argv[1], fl_name)) == False:
            if "." in fl_name:
                extensions.add(fl_name.split(".")[-1])
    sorted_list = sorted(extensions)
    print(sorted_list)
    return sorted_list

def ex5(target, to_search):
    files_list = []
    try:
        if os.path.isdir(target):
            for (root,directories,files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root,fileName)
                    f = open(full_fileName, "rb")
                    file_content = f.read()
                    if to_search.encode() in file_content:
                        files_list.append(fileName)
        elif os.path.isfile(target):
            f = open(target, "rb")
            file_content = f.read()
            if to_search.encode() in file_content:
                files_list.append(target)
        else:
            raise ValueError("Invalid path")
    
    except ValueError as e:
        print(e)

    if len(files_list) != 0:
        print(files_list)
        return files_list
    else:
        print("Not found!")

def callback(e):
    print(str(e) + "FROM CALLBACK")

def ex6(target, to_search, cb):
    files_list = []
    try:
        if os.path.isdir(target):
            for (root,directories,files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root,fileName)
                    f = open(full_fileName, "rb")
                    file_content = f.read()
                    if to_search.encode() in file_content:
                        files_list.append(fileName)
        elif os.path.isfile(target):
            f = open(target, "rb")
            file_content = f.read()
            if to_search.encode() in file_content:
                files_list.append(target)
        else:
            raise ValueError("Invalid path")
    
    except Exception as e:
        cb(e)
    

    if len(files_list) != 0:
        print(files_list)
        return files_list
    else:
        print("Not found!")

def ex7(path):
    if os.path.isfile(path):
        result = {}
        result["full_path"] = path

        statinfo = os.stat(path)
        result["file_size"] = statinfo.st_size

        if "." in path:
            result["file_extension"] = path.split(".")[-1]
        else:
            result["file_extension"] = ""
        
        result["can_read"] = os.access(path, os.R_OK)

        result["can_write"] = os.access(path, os.W_OK)

        print (result)
        return result
    else:
        print("not file")
        return -1

def ex8(dir_path):
    result = []
    if os.path.isdir(dir_path):
        content_list = os.listdir(dir_path)
        for item in content_list:
            if os.path.isfile(item):
                result.append(os.path.join(dir_path,item))
        print (result)
        return result
    else:
        print("wrong path")
        return -1

if __name__ == '__main__':
    #ex1("D:\\Desktop")
    #ex2("D:\\Desktop", "D:\\Desktop\\fisiere.txt")
    #ex3("D:\\Desktop")
    #ex4()
    #ex5("D:\\Desktop\\fisiere.txt", "G")
    ex6("D:\\Desktop\\fisiere", "G", callback)
    #ex7("D:\\Desktop\\fisiere.txt")
    #ex8("D:\\Desktop")