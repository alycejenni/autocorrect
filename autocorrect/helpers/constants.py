import re
from collections import namedtuple

TypeNames = namedtuple('TypeNames', 'strings ascii comment documentable imports')
typenames = TypeNames(**{
    'strings': ['string', 'unicodestring', 'rawstring', 'binarystring',
                'unicoderawstring', 'binaryrawstring'],
    'ascii': ['string'],
    'comment': ['comment'],
    'documentable': ['def', 'class'],
    'imports': ['import', 'fromimport']
    })

Regexes = namedtuple('Regexes', 'single_quote triple_quote prefix content')
regex = Regexes(**{
    'single_quote': re.compile('(?:^([A-Za-z]+)?(\")(?!\"{2}))|((?<!\"{2})\"$)'),
    'triple_quote': re.compile('(?:^([A-Za-z]+)?(\"){3})|(\"{3}$)'),
    'prefix': re.compile('(?:^([A-Za-z]*)(?=[\"\']))'),
    'content': re.compile('(?:^[A-Za-z]*([\'\"]{1,3}))(?P<content>.*?)([\'\"]{1,3})$')
    })


