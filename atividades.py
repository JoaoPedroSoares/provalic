with open ('series.csv', 'r', encoding='utf-8')as file:
    def verificar_ano():
        for line in file:
            coluna = line.split(',')
            colunaz = coluna[3].split(' ')
            data = data.split (' ')

            if colunaz[2] == data[2]:
                print(colunaz[2])
            else:
                pass



    def imdb10():
        for line in file:
            coluna = line.split(',')
            if coluna[5] == '10' and coluna[6] == '10':
                print ('serie :', coluna[0], '\n episodio : temp ',coluna[1],', ep', coluna[2], ' \n nota IMDB:', coluna[5] ,' \n nota netflix:',coluna[6])
            else:
                pass
    
    
    def socorro()
        for line in file
            coluna = line.split(',')


print('deu tudo errado')
