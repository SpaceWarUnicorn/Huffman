import heapq

cosas = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'

def main():
    cosas2 = list(cosas)
    print (cosas2)
    listaLetras = freq(cosas2)
    arbol = ordenarLetras(listaLetras)
    #arbol = binLet(listaLetra)
    makeTree(arbol)
    #codifica(codigo,listaLetra)

"""def codifica(codigo, listaLetra):
    newStr = ''
    for v in cosas:
        newStr +=v

    print(str(codigo) +" "+ str(listaLetra))"""

def makeTree(arbol):

    heap=[]
    for v in arbol:
        heapq.heappush(heap, [v])

    while len(heap) > 1:
        childL = heapq.heappop(heap)
        childR = heapq.heappop(heap)
        freqL, labelL = childL[0]
        freqR, labelR = childR[0]

        freq = freqL + freqR

        label = ''.join(sorted(labelL + labelR))
        node = ((freq, label), childL, childR)

        heapq.heappush(heap, node)
    print('Arbol \n' + str(heapq.heappop(heap)) + '\n')



def ordenarLetras(listaLetras):
    listLet = list(set(listaLetras))
    listLet.sort(key=lambda letra: letra[0], reverse=True)
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

def freq(cosas2):
    frecuenciaLet = []
    for w in cosas2:
        frecuenciaLet.append(cosas2.count(w))
    print("Pares\n" + str(zip(cosas2, frecuenciaLet))+ "\n")
    return zip(frecuenciaLet,cosas2)

if __name__ == "__main__":
    main()
