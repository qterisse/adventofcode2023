def get_sub_lst(lst):
    sub_lst = []
    for n in range(len(lst) - 1):
        sub_lst.append(int(lst[n + 1]) - int(lst[n]))
    if (any([e != 0 for e in sub_lst])):
        get_sub_lst(sub_lst)
    lst.append(int(lst[-1]) + sub_lst[-1])
    lst.insert(0, int(lst[0]) - sub_lst[0])
    return (lst)

def part1():
    with open("day9_input") as f:
        lines = f.read().split('\n')
    
    total_part1 = 0
    total_part2 = 0
    for line in lines:
        lst = get_sub_lst(line.split(' '))
        total_part1 += lst[-1]
        total_part2 += lst[0]
    
    print(f'result part1: {total_part1}')
    print(f'result part2: {total_part2}')
    

if __name__ == "__main__":
    part1()