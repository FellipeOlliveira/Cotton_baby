import threading
import time

def semafaro1():
    lista = ['vermelho','vermelho','verde','amarelo','vermelho','vermelho']
    for i in lista:
        print(f"semafaro 1: {i}")
        time.sleep(1)  # Simula um atraso

def semafaro2():
    lista = ['verde', 'amarelo', 'vermelho','vermelho','verde','amarelo']
    for i in lista:
        print(f"semafaro 2: {i}")
        time.sleep(1)  # Simula um atraso

# Cria as threads



teste = True

repetidor = 0

while teste:
    thread1 = threading.Thread(target=semafaro1)
    thread2 = threading.Thread(target=semafaro2)
# Inicia as threads
    thread1.start()
    thread2.start()

# Aguarda ambas as threads terminarem
    thread1.join()
    thread2.join()

    if repetidor != 10:
        repetidor += 1
    else:
        break
