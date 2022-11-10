import math

def is_prime(numar):
    """"""
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False

    max = int(math.sqrt(numar)) + 1
    """
    i = 3
    while i < max:
      if numar % i == 0:
        return False
      i = i + 2
    """
    for it in range(3, max + 1, 2):
      if numar % it == 0:
        return False
    
    return True

def process_item(x):
    if x < 2:
        return -1
    else:
        x += 1
        while x :
            if is_prime(x):
                return x
            x += 1
        return -1
        
if __name__ == "__main__":
    x = input("insert number: ")
    if x.isnumeric():
        x = int(x)
        print(process_item(x))





