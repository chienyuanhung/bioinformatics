def PathToGenome(path):
    results = path[0].split('\n')[0]
    plen = len(path)
    for i in range(1, plen):
        results = results + path[i].split('\n')[0][-1]
    return results

if __name__ == '__main__':
    with open("data1.txt", 'r') as text:
        lines = text.readlines()
    seq = PathToGenome(lines)
    print(seq)

