import re


def words(string):
    _ = re.findall(r'\w{2}\S+', string)
    if _:
        return _
    return None


# def phone_numbers(string):
#     return {"area_code": "919", "number": "555-1212"}
#     # return dict([('area_code', re.search(r'^\d+', string).group(0)),
#     #            ('number', re.search(r'(\d+[-]\d+)$', string).group(0))])
#

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
