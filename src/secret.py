import aesio
from binascii import hexlify


def format_passwd(passwd):
    return "{:<16}".format(passwd[:16]).replace(' ', 'x')

def encrypt(passwd, data):
    passwd = format_passwd(passwd)
    data = format_passwd(data)
    output = bytearray(len(passwd))
    cipher = aesio.AES(passwd, aesio.MODE_CBC)
    cipher.encrypt_into(data, output)
    return output

def decrypt(passwd, data):
    passwd = format_passwd(passwd)
    output = data
    cipher = aesio.AES(passwd, aesio.MODE_CBC)
    cipher.decrypt_into(data, output)
    return output
