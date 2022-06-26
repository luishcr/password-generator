import random

def password_generator():
    MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    SYMB = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')
    letters_list = MAYUS + MINUS
    letters_nums_list = MAYUS + MINUS + NUMS
    allchars_list = MAYUS + MINUS + NUMS + SYMB
    password = []
    password_length = 0
    password_chars = ''
    

    while password_length < 8 or password_length > 99:
        password_length = int(input("""
*) Password length.
Enter a number beetwen 8 and 99:
""")) 

        while password_chars != '1' or password_chars != '2' or password_chars != '3':
            password_chars = input(""" 
*) Password characters.
Select a combination:
1. Lowercase and uppercase letters.
2. Lowercase and uppercase letters + numbers.
3. Lowercase and uppercase letters + numbers + symbols.
""") 

            if password_chars == '1':
                for i in range(password_length):
                    random_char = random.choice(letters_list)
                    password.append(random_char)
                break
            
            elif password_chars == '2':
                for i in range(password_length):
                    random_char = random.choice(letters_nums_list)
                    password.append(random_char)
                break

            elif password_chars == '3':
                for i in range(password_length):
                    random_char = random.choice(allchars_list)
                    password.append(random_char)
                break
    

    password = ''.join(password)
    return password


def run():
    password_generated = password_generator()
    print(f"""
*)  Generated password:
{password_generated}
""")


if __name__ == '__main__':
    run()