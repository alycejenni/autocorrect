import re
from types import SimpleNamespace

typenames = SimpleNamespace(**{
    'strings': ['string', 'unicodestring', 'rawstring', 'binarystring',
                'unicoderawstring', 'binaryrawstring'],
    'ascii': ['string'],
    'comment': ['comment'],
    'documentable': ['def', 'class'],
    'imports': ['import', 'fromimport']
    })

regex = SimpleNamespace(**{
    'single_quote': re.compile('(?:^([A-Za-z]+)?(\")(?!\"{2}))|((?<!\"{2})\"$)'),
    'triple_quote': re.compile('(?:^([A-Za-z]+)?(\"){3})|(\"{3}$)'),
    'prefix': re.compile('(?:^([A-Za-z]*)(?=[\"\']))'),
    'content': re.compile('(?:^[A-Za-z]*([\'\"]{1,3}))(?P<content>.*?)([\'\"]{1,3})$')
    })


