# -*- coding: utf-8 -*-
import enchant
import sys

def find_lang(k):
    inp = k.split(' ')
    d = enchant.Dict("en_US")
    c1=0
    for i in inp:
        if(len(i)>3 and d.check(i) == True):
            c1+=1            
    if(c1>=1):
        return "eng"
    else:
        return "shree"
        
def normalization(word):
    word=word.replace('अा','आ')
    word=word.replace('इर्','ई')
    word = word.replace('आै', 'औ')
    word = word.replace('अाै', 'औ')
    word = word.replace('ाै', 'ौ')
    word = word.replace('आे', 'ओ')
    word = word.replace('अौ', 'औ')
    word = word.replace('एे', 'ऐ')
    word = word.replace('ि्र', '्रि')
        
    print("Converting---")
    return word

k = sys.argv    #for command line arguments
               
f = open(str(k[1]),"r")
k1 = []
c=0
for line in f:
    if(len(line)>1):
        k1.append(line.strip())

en = {}

abcd = open("shree_encodings.txt","r")
for i in abcd:
    line = i.strip().split()
    if(len(line)==2):
        en[line[0]]=line[1]

en[" "]=" "
en[" "]="इ"

if(len(sys.argv) ==3):
    output = open(str(k[2]), "w")
else:
    output = open("output.txt","w")

full_char = ['क', 'ख', 'ग', 'घ', 'ड', 'ढ', 'च', 'छ', 'ज', 'झ','ट', 'ठ', 'न', 'ण', 'फ', 'प', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'स', 'श', 'ह', 'त', 'थ', 'द','ध','त्र', 'क्त','क्क','द्ब', 'व','ग्न','द्ध', 'ह्य', 'क्ष', 'ह्र', 'द्म', 'ट', 'त्र', 'श्व', 'श्न','श्र', 'रू', 'ड्य', 'द्भ', 'ढ्य', 'ठ', 'ड्ड', 'ट्ट', 'ट्ठ','ञ्ज', 'ञ्च', 'च्च', 'ज्ज', 'ल्ल', 'ह्न', 'ह्ण', 'ह्ल', 'ह्व', 'ड्ढ', 'ङ्क', 'ङ्ख', 'ङ्ग', 'ङ्घ', 'ङ्क्ष', 'छ्व', 'ज्ञ', 'ळ', 'हृ', 'क्व','ट्व', 'द्र', 'द्ग','श्ल','प्त', 'च्य','द्य' 'ह्म', 'स्त्र', 'ङ', 'द्द', 'द्ध', 'श्च', 'न्न', 'ऋ','व', 'ठ्य', 'द्न', 'ज़', 'ठ्ठ', 'द्व', 'रु','फ़', 'ष्ट', 'ष्ठ','ष']
half_char =['्','र्','ळ्','श्','ल्','य्','व्','द्य्','श्र्','त्त्','्ँ','ज्ञ्','ड़्क्त','ज़्','ज्ज्','च्च्','ज्','च्','म्','भ्','ब्','फ्','प्','ध्','थ्','त्','ण्','ञ्','ज्','घ्','ग्','ख्','क्','ह्म्','श्र्','ष्','स्','न्']
numbers=['1','2','3','4','5','6','7','8','9','0',':','−','/']
special_char=["आ","ो"]
for k in k1:
    lang = find_lang(k)
    if(lang == "shree"):
        char = list(k)
        word = ""
        temp, flag =-1, False
        for i in range(0,len(char)):
            if(char[i] in en):
                c =en[char[i]]
                if(c=="ि"):
                    rule1 ="ि"
                    temp=True
                elif(c=='र्' and word[-1]!="इ"):
                    count =-1
                    for i in range(len(word)):
                        if(word[count] in full_char):
                            word = word[:count]+c+word[count:]
                            break
                        count=count-1  
                elif(c=="ा" and word[-1] in half_char):
                    word=word[:-1]
                elif(c=="े" and word[-1]=="ं"):
                    word = word[:-1]+c+word[-1:]
                elif(c=="ै" and word[-1]=="ं"):
                    word = word[:-1]+c+word[-1:]
                elif(temp==True and c in full_char):
                    word = word+c+rule1
                    temp=False
                elif(c=='र्' and word[-1]==' '):
                    word=word[:-1]+'ई'
                elif(c=='इ' and word[-1] in numbers ):
                    word=word+' '
                else:
                    word = word+c
        word =normalization(word)
        output.write(word+"\n")
    else:
        output.write(k+"\n")         
