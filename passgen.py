import random

def gen_pass(n):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(n):
        password += random.choice(character)

    return password

n = int(input('enter the length of password:'))
print('your password is:', gen_pass(n))


    


