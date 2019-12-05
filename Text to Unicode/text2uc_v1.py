# -*- coding: utf-8 -*-
import nltk
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

half_char = ["*",":","<","C","G","H","M","N","R","Y","a","b","t","}","≠","Ø","¸","Ú","È","Ë","„","–","…","ø","º","E","F",'K','W','e','h','j','m','s','v','|','°','¢','§','®','©','¨','∑','∏','ª','¬','∆','«','œ','—','◊','ÿ','Â','Ï','Ì','Ô','ˆ','˜']
special_char=["आ","ो"]
for k in k1:
    lang = find_lang(k)
    if(lang == "shree"):
        char = list(k)
        word = ""
        temp, flag =-1, False
        for i in range(0,len(char)):
            if(char[i] in en):
                if(ord(char[i])==32 and char[i-1]!="–" ):
                    word =word+" "
                elif(ord(char[i])==32 and char[i-1]!="º"):
                    word=word+" "
                elif(char[i]==" " and char[i-1]=="º"):
                    continue
                elif(char[i]==" " and char[i-1]=="–"):
                    continue
                elif(char[i]=="Ø" and char[i-1]=="H"):
                    word=word[:-1]
                    word=word+en[char[i]]+en[char[i-1]]
                elif(char[i]=="*" and char[i-1]==";"):
                    word=word[:-1]
                    word=word+en[char[i]]+en[char[i-1]]
                elif(char[i-1]=="Ë" and char[i]=="£" and char[i-2]=="£"):
                    word=word[:-2]+en[char[i-1]]+word[-2:]+en[char[i]]
                elif(char[i-1]=="¿" and char[i]=="b"):
                    word=word[:-1]
                    word = word+special_char[0]
                elif(char[i-1]=="b" and char[i]=="C"):
                    if(char[i-2]=="¿"):
                        word = word+en["C"]
                    else:
                        word=word[:-1]
                        word = word+special_char[1]
                elif(char[i]=="„" or char[i]=="G" or char[i]=="<"):
                    t=char[i]
                    flag =True
                
                elif(char[i]=="∂" or char[i]=="¨" or (len(char)-i > 2 and char[i]=="–" and char[i+1]==" ")):
                    j=0
                    while(1):
                        j+=1
                        if(char[i-j] not in half_char):
                            if(char[i]=="¨"):
                                word=word[:-(j+2)]+en[char[i]]+word[-(j+2):]
                            elif(char[i-j-1]!="<"):
                                if(len(word)>=2 and word[-1]==en["G"]):
                                    word=word[:-(j+1)]+en[char[i]]+word[-(j+1):]    
                                else:
                                    word=word[:-(j)]+en[char[i]]+word[-(j):]
                            else:
                                word=word[:-(j+1)]+en[char[i]]+word[-(j+1):]
                            break
                elif(char[i] in half_char and char[i-1]=="*"):
                    word = word[:-1]
                    word = word+en[char[i]]+en[char[i-1]]    
                else:
                    word = word+en[char[i]]
                    if(flag==True and char[i] not in half_char):
                        word = word+en[t]
                        flag=False
                temp+=1
        word =normalization(word)
        output.write(word+"\n")
    else:
        output.write(k+"\n")
