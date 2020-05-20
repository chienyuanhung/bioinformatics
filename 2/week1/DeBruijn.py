from collections import defaultdict
d = defaultdict(list)

def DeBruijn(text, k):
    tlen = len(text)
    t_list = []
    for i in range(tlen-k+1):
        t_list.append((text[i:i+k-1], text[i+1: i+k]))
    d = defaultdict(list)
    for k, v in t_list:
        d[k].append(v)
    return d

if __name__ == '__main__':
    with open("data3.txt", 'r') as text:
        lines = text.readlines()
    k = int(lines[0])
    text = lines[1].split('\n')[0]

    c = DeBruijn(text, k)
    output = open("debrujin_out.txt",'w')
    keys = [key for key in c.keys()]
    keys.sort()
    for i in keys:   
        if c[i]:
            out = ','.join(c[i])
            output.writelines(i +' -> ' + out + '\n')
