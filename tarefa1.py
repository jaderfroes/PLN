# fazer expressões regulares que captam email e telefone do site da ufpel
import re

email = "t2oretorebaixado5cm@bol.com"
telefone = "12345-67890"

flag_email = re.search("^[a-z][a-z0-9]+@[a-z]+.com$", email)
flag_telefone = re.search("^[1-9][0-9]{4}-[0-9]{4}$", telefone)

if(flag_email):
    print("email válido")
else:
    print("email não aprovado")

if(flag_telefone):
    print("telefone válido")
else:
    print("telefone não aprovado")
    
# \([0-9]{2}\) \d{4}-\d{4} telefone correção
# [a-z]+@\w{3}\.\w{5}\.\w{3}.\w{2} correção email do inf
