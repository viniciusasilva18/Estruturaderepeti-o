# O loop vai rodar para sempre
while True:
    temp = float(input("Digite a temperatura: "))

    if temp > 80:
        print("ALERTA: Resfriamento ativado!")
    
    if temp == 0:
        print("Desligando...")
        break # Para o loop na hora