import re
import textminer.separator as s


def binary(string):
    return re.match(r'\b[01]+', string)


def binary_even(string):
    return re.match(r'\b[01]+0$', string)


def hex(string):
    return re.match(r'\b[0-9ABCDEF]+$', string)


def word(string):
    return re.match(r'^[0-9A-z-]+[A-z]$', string)


def words(string, count=0):
    temp = s.words(string)
    if count == 0:
        return bool(temp)
    b = [(count == len(temp))]
    for item in temp:
        b.append(word(item))
    return all(b)


def phone_number(string):
    return re.match(r'.?\d{3}.*\d{3}.?\d{4}.?', string)


# def zip_code(string):
#     if re.match(r'^(\d{5}(\-\d{4})?)$', string):
#         return True
#     return False

# print(zip_code('12345'))
# print(zip_code('12345-1234'))
# print('--------------------')
# print(zip_code('1234'))
# print(zip_code('1234512'))
# print(zip_code('1234-1212'))
# print(zip_code('12345-12123'))

# def money(string):
#     return re.match(r'^\$\d*[,\d{3}]*\.?\d{2}$', string)
#
# print(money('$4'))
# print(money('$19'))
# print(money('$19.00'))
# print(money('$3.58'))
# print(money('$1000'))
# print(money('$1000.00'))
# print(money('$5,555'))
# print(money('$5,555.55'))
# print(money('$12345577.89'))
# print('--------------------')
# print(money(''))
# print(money('$19,12'))
# print(money('$192.3'))
# print(money('$3.583'))
# print(money('$'))
# print(money('$31'))
# print(money('$$31'))
