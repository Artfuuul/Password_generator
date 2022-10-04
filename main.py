import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_"
chars = ""

pwd_quantity = int(input("Сколько паролей требуется создать?\n"))
pwd_len = int(input('Какой длины требуется пароль?\n'))
pwd_digits = input('Включить ли цифры от 0 до 9?\n').strip()
pwd_uppercase = input('Включать ли заглавные буквы? "Да/Нет"\n').strip()
pwd_lowercase = input('Включать ли прописные буквы? "Да/Нет"\n').strip()
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? "Да/Нет"\n').strip()
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? "Да/Нет"\n').strip()

if pwd_digits.lower() == 'да':
    chars += digits
if pwd_uppercase.lower() == 'да':
    chars += uppercase_letters
if pwd_lowercase.lower() == 'да':
    chars += lowercase_letters
if pwd_punctuation.lower() == 'да':
    chars += punctuation
if pwd_exceptions.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(pwd_len, chars):
    password = ''
    for j in range(pwd_len):
        password += random.choice(chars)
    return print(password)

for _ in range(pwd_quantity):
    generate_password(pwd_len, chars)

    #rofl