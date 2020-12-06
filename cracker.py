import random
import string

def password_cracker():

    pass_length = int(input("Enter your password length: "))

    _letters = string.ascii_letters
    _digits = string.digits
    _punctuations = string.punctuation

    possibilities = "{0}{1}{2}".format(_letters, 
                                        _digits, 
                                        _punctuations)

    possibilities = list(possibilities)
    random.shuffle(possibilities)
    random_pass = random.choices(possibilities, k=pass_length)
    random_pass = ''.join(random_pass)
    temp_let = ""

    print("Random password is", random_pass)

    while (temp_let != random_pass):
    
        temp_let = ""
        for letter in range(pass_length):
    
            guess_let = possibilities[random.randint(0, len(possibilities)-1)]
            #temp_let = str(guess_let) + str(temp_let)
            temp_let = str(temp_let) + str(guess_let)

    print("Password solved !\nYour password is \" {} \" ".format(temp_let))

if __name__ == "__main__":
    password_cracker()
