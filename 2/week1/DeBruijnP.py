def DeBruijnP(patterns):
    nodes = []
    rela = {}
    plen = len(patterns[0])
    for pattern in patterns: 
        nodes.append(pattern[0: plen-1])
        nodes.append(pattern[1: plen])
    snodes = set(nodes)
    for i in snodes:
        rela[i] = []
        for j in patterns:
            if i == j[0:plen-1]:
                rela[i].append(j[1:plen])
    return rela


if __name__ == '__main__':
    with open("data2.txt", 'r') as text:
        lines = text.readlines()
    
    patterns = []
    for i in lines:
        patterns.append(i.split('\n')[0])


    c = DeBruijnP(patterns)
    output = open("debrujin_P_out.txt",'w')
    keys = [key for key in c.keys()]
    keys.sort()
    for i in keys:   
        if c[i]:
            out = ','.join(c[i])
            output.writelines(i +' -> ' + out + '\n')