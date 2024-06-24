def change_num(list):
    list[5]='five'
    return list

example = [12,3,4,5,6,6,6,6,6,6]
print(change_num(example))

def change_tuple(examp):
    int_exampt=list(examp)
    int_exampt[5]='five'
    return tuple(int_exampt)
example1=(1,2,3,3,4,4,4,4,7)
print(change_tuple(example1))
