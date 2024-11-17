a = open('shed.yml', encoding="utf-8").readlines()

def ob(i,a):
    str = a[i]
    str = '  ' + (len(str)-len(str.lstrip()))*' '+'''"'''+str[(len(str)-len(str.lstrip())):str.index(':')]+'''": {'''
    a[i]=str
    i+=1
    while (len(a[i])-len(a[i].lstrip()))+2 != (len(str)-len(str.lstrip())):
        i=el_ob(i,a)
        if i >= len(a): break
    a[i-1]=a[i-1][:-1]
    a.insert(i,(len(str)-len(str.lstrip()))*' '+'},')
    return i+1

def el_ob(i,a):
    if ':\n' in a[i] and a[i+1].lstrip()[0]=='-':
        i=sp(i,a)
    elif ':\n' in a[i]:
        i=ob(i,a)
    else:
        a[i] = '  ' + (len(a[i]) - len(a[i].lstrip())) * ' ' + '''"''' + a[i][len(a[i]) - len(a[i].lstrip()):a[i].index(':')] + '''"''' + ':' + (' '+a[i][a[i].index(':')+2:len(a[i])-1] +',' if a[i][a[i].index(':')+2:len(a[i])-1].isdigit() else''' "'''+a[i][a[i].index(':')+2:len(a[i])-1]+'''",''')
        i+=1
    return i




def el_sp(i,a,col_pr):
    str =a[i]

    if ':\n' in str  and a[i+1].lstrip()[0]=='-':
        i = sp(i,a)
    elif ':\n' in str:
        i = ob(i,a)
    elif ':' in str:
        i = ob_in_sp_no_name(i,a,col_pr)
    else:
        a[i] = ('  '+a[i].replace('- ',' "',1)+'''",''').replace('\n','').replace('''"''','') if ('  '+a[i].replace('- ',' "',1)+'''",''').replace('\n','').replace('"','').replace(',','').replace(' ','').isdigit() else ('  '+a[i].replace('- ',' "',1)+'''",''').replace('\n','')
        i+=1
    return i

def ob_in_sp_no_name(i,a,col_pr):

    a.insert(i,col_pr*' '+'{')
    i+=1
    str:str=a[i]
    str = str.replace('-',' ',1)
    str = '  '+(len(str) - len(str.lstrip()))*' '+'''"'''+str[len(str) - len(str.lstrip()):str.index(':')]+'''"'''+':'+''' "'''+str[str.index(':')+2:len(str)-1]+'''",'''
    a[i]=str
    i+=1
    while len(a[i])-len(a[i].lstrip())+2==len(str)-len(str.lstrip()):
        if ':\n' in a[i] and a[i+1].lstrip()[0]=='-':
            i=sp(i,a)
        elif ':\n' in a[i]:
            i=ob(i,a)
        else:
            a[i]='  '+(+len(a[i]) - len(a[i].lstrip()))*' '+'''"'''+a[i][len(a[i]) - len(a[i].lstrip()):a[i].index(':')]+'''"'''+':'+(' '+ a[i][a[i].index(':')+2:len(a[i])-1] +',' if a[i][a[i].index(':')+2:len(a[i])-1].isdigit() else''' "'''+a[i][a[i].index(':')+2:len(a[i])-1]+'''",''')
            i+=1
        if i>=len(a):break
    a[i-1]=a[i-1][:-1]
    a.insert(i,col_pr*' '+'},')
    return i+1
def  sp(i,a):
    str = a[i]
    pr=0
    dv = 0
    for j in range(len(str)):
        if str[j]!=' ':
            pr = j
            break
    for j in range(len(str)):
        if str[j]==":":
          dv = j
          break
    str = '  ' + str[:pr]+ '''"'''+str[pr:dv]+ '''"'''+': ['
    a[i]=str
    col_pr = (len(a[i - 1]) - len(a[i - 1].lstrip()) + 1)
    i+=1
    col_do_t=len(a[i])-len(a[i].lstrip())
    while a[i].lstrip()[0]=='-' and len(a[i])-len(a[i].lstrip())==col_do_t:
        i=el_sp(i,a,col_pr)
        if i >= len(a): break
    a[i-1]=a[i-1][:-1]
    a.insert(i,(len(str)-len(str.lstrip()))*' '+'],')
    return i+1




i=0
while i < len(a):
    if ':\n' in a[i] and a[i + 1].lstrip()[0] == '-':
        i = sp(i, a)
    elif ':\n' in a[i]:
        i = ob(i, a)
    else:
        a[i] = '  ' + (len(a[i]) - len(a[i].lstrip())) * ' ' + '''"''' + a[i][len(a[i]) - len(a[i].lstrip()):a[i].index(
            ':')] + '''"''' + ':' + ' ' + a[i][a[i].index(':') + 2:len(a[i]) - 2] + '''",'''
        i += 1
a[-1]=a[-1][:-1]
a=['{']+a+['}']
print('\n'.join(a))
