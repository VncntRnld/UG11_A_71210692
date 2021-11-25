def ambildanbalik(kal,m,s,k):
    if k==True:
        return kal[m-1:s][::-1]
    else:
        return kal[m-1:s]



print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))