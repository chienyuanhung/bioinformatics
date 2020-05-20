def Overlap(Patterns):
    ol = {}
    for i in Patterns:
        ol[i] = []
        for j in Patterns:
            if i[1:] == j[0: -1]:
                ol[i].append(j)
    return ol


if __name__ == '__main__':
    with open("data2.txt", 'r') as text:
        lines = text.readlines()
    
    pattern = []
    for i in lines:
        pattern.append(i.split('\n')[0])

    c = Overlap(pattern)
    output = open("output.txt",'w')
    for i in c:
        if c[i]:
            output.writelines(i +' -> ' + c[i][0] + '\n')
