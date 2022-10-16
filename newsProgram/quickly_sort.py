def quickly_sort(local_num=None, **args):
    empty_str = ''
    now_local_num = 0
    for j in range(1, len(lis1) + 1):
        for i in lis1:
            now_local_num += 1
            if i > lis1[j]:
                empty_str = lis1[j]
                lis1[j] = i
                empty_str = i
        else:
            break
    return lis1


if __name__ == '__main__':
    list1 = ['2', '3', '6', '1', '8', ' 7', '10', '9', '0']
    quickly_sort(list1)
