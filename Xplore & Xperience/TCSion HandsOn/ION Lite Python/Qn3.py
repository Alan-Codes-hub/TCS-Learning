def find_Novowels(inp_str):
    vowels=['a','e','i','o','u']
    output=[]
    for string in inp_str:
        if any(vowel in string for vowel in vowels)==True:
            output.append(string)
    return output

if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
            inp_str.append(input())
    output=find_Novowels(inp_str)
    if len(output)!=0:
        print('Strings without vowels:')
        for i in output:
                print(i)
    else:
        print('No string found')


        
