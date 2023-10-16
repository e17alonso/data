import re
def placas(placa):
    p=r'^P\d\d\d[A-Z][A-Z][A-z]'
    return(re.findall(p,placa))

def archivo(string):
    p=r'.pdf$|.jpg$'
    return(re.findall(p,string))

def contraseña(string):
    c=r'\w'
    m=r'[A-Z]'
    patron = r'[^a-zA-Z0-9\s]'
    caracteres=re.findall(c,string)
    mayusculas=re.findall(m,string)
    especiales=re.findall(patron,string)
    return(caracteres,mayusculas,especiales)

def correo(string):
    p=r'@ufm.edu$'
    return(re.findall(p,string))


def carne(string):
    p = r'([0-3][0-9])(00)(1[1-9][1-9][0-9]|[2-7][0-9]{3}|[8][0-9][0-7][0])'
    return re.findall(p, string)

def numero(string):
    p = r'((\+502|502)?(\s)?(4|5|6|2)(\d\d\d)(-|\s)?(\d\d\d\d))'
    return(re.findall(p,string))

string1="P096FZL"
string2='foto.jpg'
string3='#Contraseña123'
string4='rolandoalonso@ufm.edu'
string5='19001234'
string6='+50254821151, 4210-7640, 52018150, 2434 6854, 11234569, 50211234578'

if placas(string1):
    print('Placa válida')
else:
    print('Placa inválida')


if archivo(string2):
    if archivo(string2)[0]=='.pdf':
       print('Es un archivo pdf')
    elif archivo(string2)[0]=='.jpg':
        print('Es un archivo jpg')
else:
    print('Es un archivo inválido')


c,m,e=contraseña(string3) 
if(len(c)>=8 and len(m)>=1 and len(e)>=1):
    print('Contraseña válida')
else:
    print('Contraseña inválida')


if correo(string4):
    print('Correo proveniente de la ufm')
else:
    print('Correo proveniente de otra institución')


if carne(string5):
    print('carné válido')
else:
    print('carné inválido')

print(numero(string6))