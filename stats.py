def word_count(text):
    word_list=text.split()
    words=len(word_list)
    
    return words

def character_count(text):
    ltext=text.lower()
    word_numb ={}
    for i in ltext:
        if i in word_numb:
            word_numb[i]+=1
        else:
            word_numb[i]=1
    return word_numb

def sort_on(items):
    return items["num"]

def sor_list(dict):
    big_list=[]
    for key,value in dict.items():
        if key.isalpha():
            smol_dict={"char":key,"num":value}
            big_list.append(smol_dict)
    big_list.sort(reverse=True,key=sort_on)
    return big_list
    