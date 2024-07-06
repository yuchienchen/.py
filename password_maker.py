def make_password(string):
    password = string.replace('a', '@').replace('i', '!').replace('o', '0').replace('A', '@').replace('I', '!').replace('O', '0')
    return password

print(make_password("acbiouABCIOU"))
