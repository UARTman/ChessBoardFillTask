def Show_screen(Field):
    for i in range(len(Field)):
        print(i+1, '', end = '')
        for k in Field[i]:
            print(k, end = '')
        print()
    return True


Show_screen([[0, 0, 0], [1, 1, 1], [1, 2, 3]])
