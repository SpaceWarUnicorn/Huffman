import heapq


def main():
    message = extractText()
    text2 = list(message)
    listletter = freq(text2)
    preTree = ordenarLetras(listletter)
    Tree = makeTree(preTree)
    print('Tree')
    print(Tree)
    Code = creatCode(Tree)
    print('\nDictionary')
    print (Code)
    enc = encode(Code, message)
    print('\nCompressed message')
    print(enc)
    deco= decoding(enc, Code)
    createDecode(deco)
    print('\nDecompressed message\n'+deco)

def createDecode(deco):
    with open('decoding.txt',"w") as f:
        data = f.write(deco)
    print 'success'

def extractText():
    with open('text.txt') as f:
        data = f.read()
    print data
    return str(data)

def decoding(enc, Code):
    bits = ''
    msj = ''
    for bit in enc:
        bits += bit
        if([ key for key,val in Code.items() if val == bits] != []):
            msj += ''.join([ key for key,val in Code.items() if val == bits])
            bits=''
    return msj

def encode(Code, message):
    return ''.join([ Code[letter] for letter in message])

def creatCode(Tree):
    code = dict()
    mapTree(Tree, code, '')
    return code

def mapTree(Tree, code, binary):
    if(len(Tree) == 1):
        freq, label = Tree[0]
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
''' references : https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/ '''
