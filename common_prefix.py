# longest_common_prefix
def main():
    pass
    n=int(input())
    list_1=[]
    inp_2=[]
    final=[]
    temp=[]
    flag=0
    for i in range(n):
        list_1.append(input())
    if(n<=2):
        wor=list(list_1[0])
        worr=list(list_1[1])
        for wo,wo1 in zip(wor,worr):
            if(wo==wo1):
                inp_2.append(wo)
            else:
                break
        print(''.join(inp_2))
    elif(n>2):
        wor=list(list_1[0])
        for i in range(1,len(list_1)):
            for j in range(2,len(list_1)):
                wor1=list(list_1[i])
                wor2=list(list_1[j])
            for w,w1,w2 in zip(wor,wor1,wor2):
                if(w==w1==w2):
                    final.append(w)
                if(w!=w1!=w2):
                    break
        for ww,ww1 in zip(wor,final):
            if(ww==ww1):
                temp.append(ww)
        print(''.join(temp))
if __name__ == '__main__':
    main()
