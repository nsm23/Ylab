from ipaddress import IPv4Address


def int32_to_ip(data):
    return str(IPv4Address(data))
    

