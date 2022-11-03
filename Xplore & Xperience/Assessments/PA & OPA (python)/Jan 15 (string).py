
def word_occurence_dict(str_in):
    list=str_in.split()
    dict={}
    for i in list:
        dict[i]=list.count(i)
    return dict

def max_count_word(string_in):
    out=word_occurence_dict(string_in)
    output=sorted(out,key=lambda x:out[x],reverse=True)
    return output[0]

if __name__=='__main__':
    res1=max_count_word('Good morning Good evening')
    res2=max_count_word('Hello Bye Hi TCS Hello Xplore Hello Bye')
    print(res1)
    print(res2)
