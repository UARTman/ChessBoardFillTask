def generation(a, b):
    field = []
    for i in range(a):
        field.append([0 for k in range(b)])
    return field
def upload():
    f = open('settings.txt', 'r')
    temp = []
    str_a = f.read(1)
    s = f.read(1)
    str_b = f.read(1)
    return int(str_a), int(str_b)
