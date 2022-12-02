import random
import base64
from time import sleep

def feliz_cumpleaños():
    familiares_e = [b'TWFtw6E=', b'UGFww6E=', b'TWlndWVs', b'TGVpZHk=', b'Tmljbw==', b'RGllZ28=', b'VG9iYnk=', b'UGFjaGl0YQ==', b'U2Nvb2J5']
    deseos_e = [b'bXVjaGEgU2FsdWQgIOKalSDwn5KaIPCfj4Pwn4+K8J+kuA==', 
              b'cXVlIERpb3MgdGUgYmFuZGlnYSBlbiB0b2RvIGxvIHF1ZSBoYWdhcyDwn5mPIPCfmIc=', 
              b'bXVjaG8gQW1vciwgTWkgQW1vb29yLCBtbW1tbW1tIPCfkpgg8J+SlSDwn5KP', 
              b'dW5hIHZpZGEgTGFyZ2EsIFZhbGllbnRlIHkgVmljdG9yaW9zYSDwn5KqIPCfj4Y=', 
              b'RGlzY2VybmltaWVudG8geSBTZXJlbmlkYWQg4pqWIPCfk5Ag8J+nmA==', 
              b'MTAgTWlsbG9uZXMgZGUgRMOzbGFyZXMgQ29tcGFhYWRyZSDwn5Kw8J+SsPCfkrAg8J+TiCDwn6SR', 
              b'U2FiaWR1csOtYSDwn6STIPCfk5Yg8J+TmiAuLi4gT3llLCDCv21lIGRhcyB1biB0cmljaXRvIGRlIHRvcnRpdGE/IPCfjbAg8J+Qtg==', 
              b'bXVjaGEgQWJ1bmRhbmNpYSDwn5iOIPCfkZHwn5KOIPCfpanwn6WX', 
              b'cXVlIGVsIGNpZWxvIHRlIHRyYWlnYSBtdWNoYSBGZWxpY2lkYWQg8J+YgyDwn5iEIPCfmIEg8J+YgiA=']
    porcentaje_revolver=99
    if random.random() < porcentaje_revolver/100:
        #random.shuffle(deseos_e)
        random.shuffle(familiares_e)     
    print("\n\n\U0001F382 \U0001F382 Feliz Cumpleaños JuanDa!!!\n")
    sleep(4)
    print("Tu familia te ha enviado unos bellos deseos.")
    sleep(3)
    print(f"Pero creo que se me han revuelto \U0001F926, esto me pasa el {porcentaje_revolver}% de las veces \U0001F937:\n")
    sleep(4)
    familiares = [base64.b64decode(familiar).decode('utf-8') for familiar in familiares_e]
    deseos = [base64.b64decode(deseo).decode('utf-8') for deseo in deseos_e]
    for familiar,deseo in zip(familiares,deseos):
        print(f"  {familiar} te desea...")
        sleep(3)
        print(f"    {deseo}\n")
        sleep(5)
    print("Ay! noo, así no eran, qué enredo \U0001F92A")
    print("  Menos mal los imprimí, mira tu tarjeta de ragalo.")

feliz_cumpleaños()



'''
    familiares = ['Mamá', 'Papá', 'Miguel', 'Leidy', 'Nico', 'Diego', 'Tobby', 'Pachita', 'Scooby']
    deseos = ['Que el cielo te traiga mucha Felicidad \U0001F603 \U0001F604 \U0001F601 \U0001F602',
            'Que Dios te bendiga en todo lo que hagas \U0001F64F \U0001F607', 'Una vida Larga, Valiente y Victoriosa \U0001F4AA \U0001F3C6', 
            'Mucha Salud  \U00002695 \U0001F49A \U0001F3C3\U0001F3CA\U0001F938', 'Discernimiento y Serenidad \U00002696 \U0001F9D0 \U0001F9D8 ', 
            'Mucha Abundancia \U0001F60E \U0001F451\U0001F48E \U0001F969\U0001F957', 
            '10 Millones de Dólares Compaaadre \U0001F4B0\U0001F4B0\U0001F4B0 \U0001F4C8 \U0001F911', 
            'Mucho Amor, Mi Amooor, mmmmmmm \U0001F498 \U0001F495 \U0001F48F', 
            'Sabiduría \U0001F913 \U0001F4D6 \U0001F4DA ... Oye, ¿me das un tricito de tortita? \U0001F370 \U0001F436']
'''

