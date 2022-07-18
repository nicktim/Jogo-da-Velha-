from Jogo_da_velha import criarBoard, fazMovimento, printBoard, getInputValido, verificaMovimento, verificaGanhador

jogador = 0 # jogador 1
board = criarBoard()
ganhador = verificaGanhador(board)

while (not ganhador):
    printBoard(board)
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")
    
    if (verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("A posição infomrada ja está ocupada")

    ganhador = verificaGanhador(board)

print("===================")
printBoard(board)
print("ganhador = ", ganhador)
print("===================")
