import re


def words(string):
    _ = re.findall(r'\w{2}\S+', string)
    if _:
        return _
    return None


def phone_number(string):
    if len(string) < 10:
        return None
    rd = dict([('area_code', re.search(r'\d{3}', string).group(0)),
              ('number', re.search(r'\d{3}[\.-]?\d{4}$',
               string).group(0))])
    rd['area_code'] = rd['area_code'][0:3]
    rd['number'] = rd['number'][0:3]+'-'+rd['number'][-4:]
    return rd

# print(phone_number('111-555-1212'))
# print(phone_number('(222) 555-1212'))
# print(phone_number('3335551212'))
# print(phone_number('444 555-1212'))
# print(phone_number('555.555.1212'))
# print(phone_number('666-1212'))


# def money(string):
#     if string[0] not in ['$']:
#         return None
#     rd = dict('currency', string[0])
#     string = string[1:]
#     rd['amount'] =
#     rd['area_code'] = rd['area_code'][0:3]
#     rd['number'] = rd['number'][0:3]+'-'+rd['number'][-4:]
#     return rd
"""
\w+\S+\D+

\w+\s*
\w+\s*\w+
\w+\s*\w+
\w+\S\w+\s*\w+
\w+\s*


\d digit            \D non-digit
\w alphanumeric     \W non-alphnum
\s whitespace       \S nonwhitespace

*   0+
+   1+
?   0-1
{n} n
{n,m} n-m
"""
