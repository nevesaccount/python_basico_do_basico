def jogar():
    print("_________________________________________")
    print("_______Bem-vindo ao Jogo da Forca!_______")
    print("_________________________________________")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra??")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letrea {} na posição {}".format(chute, index))
            index = index + 1

        print("Jogando . . .") 
    