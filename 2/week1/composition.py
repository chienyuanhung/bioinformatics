
def Composition(text, k):
    tlen = len(text)
    compo = []
    for i in range(tlen -k +1):
        pt = text[i: i+k]
        compo.append(pt)
    return compo

if __name__ == '__main__':
    with open("data.txt", 'r') as text:
        lines = text.readlines()
    k = int(lines[0])
    text = lines[1].split('\n')[0]
    No=Composition(text,k)
    txt = '\n'.join(No)                         # convert list to text with new line in-between
    file2 = open("W1-test1output1.txt", "w")
    file2.write(txt)
    file2.close()
    