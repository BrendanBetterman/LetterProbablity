import math
def countLetters(word):
    count = []
    letter =[]
    for i in word:
        found = False
        for u in range(len(count)):
            if i == letter[u]:
                found = True
                location = u
        if found:
            count[location] +=1
        else:
            count.append(1)
            letter.append(i)
    out =[]
    for i in range(len(count)):
        out.append([letter[i],count[i]])
    return out
def fac(n):
    if(n<=1):
        return 1
    else:
        return fac(n-1)*n
def ncr(n,r):
    return fac(n)/(fac(r)*fac(n-r))
def main():
    inp = input()
    inp = countLetters(inp)
    inp2 = input()
    inp2 = countLetters(inp2)
    out =1
    for i in range(len(inp2)):
        for u in range(len(inp)):
            if inp2[i][0] == inp[u][0]:
                out *= ncr(inp[u][1],inp2[i][1])
    if out <= 1:
        out =0
    print(int(out))
main()