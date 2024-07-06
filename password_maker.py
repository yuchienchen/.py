def make_password(string):
    password = string.replace('a', '@').replace('i', '!').replace('o', '0').replace('A', '@').replace('I', '!').replace('o', '0')
    return password

def main():
    string = input("")
    make_password(string)



if __name__ == "__main__":
    main()