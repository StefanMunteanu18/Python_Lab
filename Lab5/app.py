import utils

if __name__ == "__main__":
    inp = "a"
    while inp != 'q':
        inp = input("waiting for input: ")
        if inp.isnumeric():
            inp = int(inp)
            print(utils.process_item(inp))