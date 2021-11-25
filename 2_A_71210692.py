def ambil_huruf(text, lompat):       
    return text[int(len(text)/2+lompat)]

print(ambil_huruf("abcdefg",1))
print(ambil_huruf("abcdefg",2))
print(ambil_huruf("abcd",0))
