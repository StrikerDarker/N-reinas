import pandas, numpy
from sys import exit

def readBoard(path):
    try:
       archive = pandas.read_csv(path, sep = ",", header=None)
    except Exception:
        print('No such file or directory')
    else:
        return validateBoard(archive)

def validateBoard(board):
    tamBoard = numpy.shape(board)
    if(tamBoard[0] == tamBoard[1]):
        cantQueens = 0
        for i in range(tamBoard[0]):
            for j in range(tamBoard[1]):
                if(board[i][j] == 1):
                    cantQueens += 1
                    if(cantQueens > tamBoard[0]):
                        print('number of queens exceeds the limit')
                        exit()
        if(cantQueens < tamBoard[0]):
            print('number of queens is insufficient')
            exit()
        return board    
    else:
        print('wrong board size, enter NxN board')
        exit()