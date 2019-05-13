def check_symbol(mas,symb,i1,j1): #наличие нужного символа в заданной ячейке
    if mas[i1][j1] == symb:
        return 0
    else:
        return 1
def end_of_game (array,symb,n_row,n_col):#array,symbol of empty field, number of rows, number of columns
    answer=1

    for i in range (n_row):
        for j in range(n_col):
            check=check_symbol(array,0,i,j)
            if check==0:
                answer=0
                
    if answer==0:
        return True
    else:
        return False


#mas=[[1,1,1], [1,1,1],[1,1,1]]
#a=end_of_game (mas,0,3,3)
#print(a)
