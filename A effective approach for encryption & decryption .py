def get_task():
    task = input('Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = input('Enter the secret message: ')
    return message

def get_key():
    key = int(input('Enter the secret key: '))
    return key

def get_keylength (inp):
    if len(inp)%2==0:
        keylength=len(inp)/2

    else:
        keylength=(len(inp)+1)/2
    return keylength

def convert_deci(inp):
    import string
    dict={}
    bool = False
    list_con = []
    for i,char in enumerate(string.ascii_lowercase):
        dict[i]=char
    for val in inp:
        if(val.isdigit()):
            print("sorry not convert")
            bool = True
            break
        for key, value in dict.items():
            if(val== value):
                 list_con.append(str(key+1))
    return list_con

def formula(inp,con_str):
    list_form = []
    l1 = int(inp)
    length = len(con_str)
    for count in range (0,length):
        l2 = int(con_str[count])
        result = (l2 + l1)%26
        list_form.append(result)
    return list_form

def deci_to_char(inp):
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list_char = []
    for count in range(len(inp)):
        x=int(inp[count])
        y=int(x-1)
        if x == 0:
            z = list[0]
            list_char.append(z)
        else:
            z = list[y]
            list_char.append(z)
    return list_char

def encryptrailfence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
                output = ("" . join(result))
    return output

def ascii_deci(inp):
    list_asciid = []
    for count in range(0,len(inp)):
        y = ord(inp[count])
        list_asciid.append(y)
    return(list_asciid)

def flip(c):
    return '1' if (c == '0') else '0'

def binary_comp(inp):
    list_bin = []
    for count in range (0,len(inp)):
        x = (bin(inp[count])[2:].zfill(7))
        one = ' '
        for i in range (len(x)):
            one += flip(x[i])
        list_bin.append(one)
    return list_bin

def bin_to_deci(inp):
    list_deci = []
    l=len(inp)
    for count in range(l):
        n=str(inp[count])
        y=int(n,2)
        list_deci.append(y)
    return list_deci

def cipher(inp):
    list_cipher=[]
    l=len(inp)
    for count in range(l):
        x=inp[count]
        y=chr(x)
        list_cipher.append(y)
    return list_cipher

def decryptrailfence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []

    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
        output = ("".join(result))

    return output

def reverse_formula(inp,key_length):
    list=[]
    list1=[]
    list_rev = []
    length = len(inp)
    for count in range (0,length):
        l1 = inp[count]
        l2 = int(l1)
        for count in range(0,2):
            x = (26*count)+l2-key_length
            if x >0:
                list.append(x)
            else:
                list1.append(x)  
        y=min(list)
        list=[]
        list_rev.append(y)
    return list_rev

def de_deci_to_char(inp):
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list_char = []
    for count in range(len(inp)):
        x=int(inp[count])
        y=int(x-1)
        if x == 0:
            z = list[0]
            list_char.append(z)
        else:
            z = list[y]
            list_char.append(z)
        out=("" . join(list_char))
    return out

def decryption():
    message=['\x06', '\x11', '\x14', '\x11', '\x17', '\x18', '\x1d', '\x07', '\x18', '\x1e', '\x0c', '\x0c']
    key_length = get_keylength(message)
    list_asciid = ascii_deci(['\x06', '\x11', '\x14', '\x11', '\x17', '\x18', '\x1d', '\x07', '\x18', '\x1e', '\x0c', '\x0c'])
    list_bin = binary_comp(list_asciid)
    list_deci = bin_to_deci(list_bin)
    list_cipher = cipher(list_deci)
    output = decryptrailfence(list_cipher,key)
    list_con = convert_deci(output)
    list_rev = reverse_formula(list_con,key_length)
    list_char = de_deci_to_char(list_rev)
    return list_char

def encryption():
    key_length = get_keylength(message)
    list_con = convert_deci(message)
    list_form = formula(key_length,list_con)
    list_char = deci_to_char(list_form)
    output = encryptrailfence(list_char,key)
    list_asciid = ascii_deci(output)
    list_bin = binary_comp(list_asciid)
    list_deci = bin_to_deci(list_bin)
    list_cipher = cipher(list_deci)
    return list_cipher

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        key = get_key()
        encrypted =encryption()
        print('Ciphertext of the secret message is:', encrypted)

    elif task == 'decrypt':
        #message = get_message()
        key = get_key()
        decrypted = decryption()
        print('plaintext of the secret message is:', decrypted)

    else :
        break