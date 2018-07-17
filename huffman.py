import heapq

text = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'

def main():
    text2 = list(text)
    listletter = freq(text2)
    preTree = ordenarLetras(listletter)
    print('\n')
    Tree = makeTree(preTree)
    print(Tree)
    print('\n')
    Code = creatCode(Tree)
    print (Code)
    #codifica(codigo,listaLetra)

def creatCode(Tree):
    code = dict()
    mapTree(Tree, code, '')
    return code

def mapTree(Tree, code, binary):
    print(len(Tree), Tree)
    if(len(Tree)==1):
        freq,label = Tree[0]
        code[label] = binary
    else:
        value, childL, childR = Tree

        mapTree(childL, code, binary +"1")
        mapTree(childR, code, binary +"0")

    return code

def makeTree(tree):

    heap=[]
    for leaf in tree:
        heapq.heappush(heap, [leaf])

    while len(heap) > 1:
        childL = heapq.heappop(heap)
        childR = heapq.heappop(heap)
        freqL, labelL = childL[0]
        freqR, labelR = childR[0]

        freq = freqL + freqR
        label = ''.join(sorted(labelL + labelR))
        node = ((freq, label), childL, childR)

        heapq.heappush(heap, node)


    return heapq.heappop(heap)



def ordenarLetras(listLetter):
    listLet = list(set(listLetter))
    listLet.sort(key=lambda letter: letter[0], reverse=True)
    print ("ordenada \n"+str(listLet) + "\n")
    return listLet


def freq(text2):
    freqLet = []
    for w in text2:
        freqLet.append(text2.count(w))
    print("Pares\n" + str(zip(text2, freqLet))+ "\n")
    return zip(freqLet,text2)

if __name__ == "__main__":
    main()
