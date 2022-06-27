from urllib.parse import urlparse

"""Решение с помощью встроенной библиотеки"""


def domain_name(data: str) -> str:
    if urlparse(data).netloc == '':
        name = urlparse(data).path
        start = name.find('.')
        end = name.rfind('.')
        return name[start + 1:end]
    else:
        name = urlparse(data).netloc
        end = name.find('.')
    return name[:end]
    
#_______________________________________#

"""Решение стандартными методами строк"""


def domain_name(url: str) -> str:
    domain = ''
    url.lower()
    if url.startswith("hhtp://www") or url.startswith("hhtps://www"):
        start_url = url.find('.')
        for i in (url[start_url:]):
            while i != '.':
                domain += i
        return domain
    elif url.startswith('http://') or url.startswith('https://'):
        start = url.find('/')
        end = url.find('.')
        return url[start + 2:end]
    elif url.startswith('www'):
        domain = url[4:]
        end = domain.find('.')
        return domain[:end]
    else:
        end = domain.find('.')
        return domain[:end]
