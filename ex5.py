fname = input('Enter File: ')
if len(fname) < 1 : fname = "hey.txt"
hand = open(fname)

book = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        book[w] = (book.get(w, 0) + 1)


largest = 0
word = None
for k,v in book.items():
    if largest == 0 or largest < v:
        largest = v
        word = k
print(word, largest)
