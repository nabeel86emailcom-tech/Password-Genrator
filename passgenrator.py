import random
import string

def passGenerator():
    length = int(input("Please Enter Length of Password your want:"))
    chars = string.ascii_letters + string.digits + string.punctuation
    genpass = ''.join(random.choice(chars) for _ in range(length))
    print("Genrated Password is ", genpass)

passGenerator()