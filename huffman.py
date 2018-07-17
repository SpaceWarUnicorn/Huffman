import heapq

text = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'

def main():
    cosas2 = list(text)
    listletter = freq(cosas2)
    preTree = ordenarLetras(listletter)
    #arbol = binLet(listaLetra)
    Tree = makeTree(preTree)
    #codifica(codigo,listaLetra)

"""def codifica(codigo, listaLetra):
    newStr = ''
    for v in cosas:
        newStr +=v

    print(str(codigo) +" "+ str(listaLetra))"""

def makeTree(tree):

    heap=[]
    for leave in tree:
        heapq.heappush(heap, [leave])

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

"""def binLet(listaLetra):
    binVal = []
    for index in enumerate(listaLetra, start=0):
        print(index[1])
        binVal.append(bin(index[0]))
[('f', 45),('e', 16),('d', 13),('c', 12),('b', 9),('a', 5)]

    print("Codigo \n" + str(zip(listaLetra, binVal)) + "\n" )
    return binVal"""

def freq(text2):
    freqLet = []
    for w in text2:
        freqLet.append(text2.count(w))
    print("Pares\n" + str(zip(text2, freqLet))+ "\n")
    return zip(freqLet,cosas2)

if __name__ == "__main__":
    main()
