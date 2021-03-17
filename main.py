output_list = []
temp_input = []
def swapListEl(in_list, i, j):
    temp = in_list[i]
    in_list[i] = in_list[j]
    in_list[j] = temp

def permutacje_bez_powt(input_list,size):
    if size == 1:
        output_list.append(list(input_list))
        #print(output_list)

    else:
        for i in range (0,size):
            permutacje_bez_powt(input_list,size-1)

            if size % 2:
                swapListEl(input_list,0,size-1)
            else:
                swapListEl(input_list,i,size-1)


def genList(n):
    for i in range (1,n+1):
        temp_input.append(i)

if __name__ == '__main__':
    counter = 0
    genList(3)
    permutacje_bez_powt(temp_input, len(temp_input))
    for i in output_list:
        print(i)
        counter = counter + 1

    print("Liczba permutacji:", counter)







