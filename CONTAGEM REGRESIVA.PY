import time

def contagem_regressiva(tempo):
    while tempo:
        mins, secs = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tempo -= 1
    print("Contagem regressiva concluída!")

tempo = input("Digite a quantidade de segundos para a contagem regressiva: ")
contagem_regressiva(int(tempo))