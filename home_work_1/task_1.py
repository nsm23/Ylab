import re


def domain_name(url):
    url_name = r'(https?://)?(www.)?([A-Za-z_0-9-]+).*'
    return re.search(url_name, url).group(3)


def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]






