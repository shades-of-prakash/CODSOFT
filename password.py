from colorama import init,Fore,Style # type: ignore
import re
import random
def color_it(str,color):
    return getattr(Fore,color.upper())+str+Style.RESET_ALL
def visual(points):
    bar_length=10
    if points>=6:
        bar=Fore.GREEN+'='*(points)+Style.RESET_ALL+'-'*(bar_length-points)
        print(color_it('Password is Excellent','magenta'))
    else:
        bar=Fore.RED+'='*(points)+Style.RESET_ALL+'-'*(bar_length-points)
        print(color_it('Password is weak','red'))
    return f"[{bar}]({points}/10)"
def password_generator(length,add_uppercase,add_lowercase,add_numbers,add_special):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits='0123456789'
    specials='!@#$%^&*()_+[]{}|;:,.<>?'
    choice=''
    password=''
    if length>=4:
        if add_lowercase:
            password+=random.choice(lowercase)
            choice+=lowercase
        if add_uppercase:
            password+=random.choice(uppercase)
            choice+=uppercase
        if add_numbers:
            password+=random.choice(digits)
            choice+=digits
        if add_special:
            password+=random.choice(specials)
            choice+=specials
        password+=''.join(random.choice(choice) for _ in range(length-len(password)))
        return password
    else:
        if length<=3 and add_lowercase and add_lowercase and add_numbers and add_special:
            print('Given Length is {} but your requesting greater than {}'.format(length,length))
        print('So we generated a new password without complexity:')
        password+=''.join(random.choice(choice) for _ in range(length))
        return password
def password_strength_measure(password):
    points=0
    length=len(password)
    if length>=8:
        points+=6
    if re.search(r'[a-z]',password):
        points+=1
    if re.search(r'[A-Z]',password):
        points+=1
    if re.search(r'[0-9]',password):
        points+=1
    if re.search(r'[^a-zA-Z0-9\s]',password):
        points+=1
    return points
print(color_it('Welcome to Password Generator','Green'))
length=int(input(color_it('Enter the length of the password {}:'.format(color_it('(we recommend length:8 for good password)','black')),'blue')))
add_uppercase=input(color_it('Include uppercase letters?(Y/N):','Blue')).lower()=='y'
add_lowercase=input(color_it('Include lowercase letters?(Y/N):','Blue')).lower()=='y'
add_numbers=input(color_it('Include numbers?(Y/N):','Blue')).lower()=='y'
add_special=input(color_it('Include special characters?(Y/N):','Blue')).lower()=='y'
password=password_generator(length,add_uppercase,add_lowercase,add_numbers,add_special)
print("Generated Password:",password)
check_password=input(color_it('Do you want to Check the password strength(Y/N):','Green'))=='y'
if(check_password):
    print(color_it('Password strength Checker:','Green'))
    points=password_strength_measure(password)
    print('Password Strength:',visual(points))

