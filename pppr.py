a = open('shed.yml', encoding="utf-8").readlines()
import re
import json
def ob(i,a):
    str = a[i]
    obr={}
    i+=1
    while (len(a[i])-len(a[i].lstrip())) > (len(str)-len(str.lstrip())):
        obr[a[i].lstrip().replace(':','&&',1).split('&&')[0]],i=el_ob(i,a)
        if i >= len(a): break
    return obr,i+1

def el_ob(i,a):
    r =0
    if ':\n' in a[i] and a[i+1].lstrip()[0]=='-':
        r,i=sp(i,a)
    elif ':\n' in a[i]:
        r,i=ob(i,a)
    else:
        r=a[i].lstrip().replace(':','&&',1).split('&&')[1]
        i+=1
    return r,i




def el_sp(i,a,col_pr):
    str =a[i]
    r=0
    if ':\n' in str  and a[i+1].lstrip()[0]=='-':
        r,i = sp(i,a)
    elif ':\n' in str:
        r,i = ob(i,a)
    elif ':' in str:
        r,i = ob_in_sp_no_name(i,a,col_pr)
    else:
        r = a[i].replace('-','',1).lstrip()
        i+=1
    return r,i

def ob_in_sp_no_name(i,a,col_pr):
    obr ={}
    str:str=a[i]
    ptr = str.replace('-',' ',1)
    a[i]=ptr
    while len(a[i])-len(a[i].lstrip())>len(str)-len(str.lstrip()):
        if ':\n' in a[i] and a[i+1].lstrip()[0]=='-':
            obr[a[i].lstrip().split(':')[0]],i=sp(i,a)
        elif ':\n' in a[i]:
            obr[a[i].lstrip().replace(':','&&',1).split('&&')[0]],i=ob(i,a)
        else:
            obr[a[i].lstrip().replace(':','&&',1).split('&&')[0]]=a[i].lstrip().replace(':','&&',1).split('&&')[1].lstrip().replace('\n','')
            i+=1
        if i>=len(a):break
    return obr,i
def  sp(i,a):
    str = a[i]
    obr = []
    col_pr = (len(a[i - 1]) - len(a[i - 1].lstrip()) + 1)
    i+=1
    col_do_t=len(a[i])-len(a[i].lstrip())
    while a[i].lstrip()[0]=='-' and len(a[i])-len(a[i].lstrip())==col_do_t:
        t,i=el_sp(i,a,col_pr)
        obr.append(t)
        if i >= len(a): break
    return obr,i


def star(a):
    drev = {}
    i=0
    while i < len(a):
        if ':\n' in a[i] and a[i + 1].lstrip()[0] == '-':
            drev[a[i].lstrip().replace(':','&&',1).split('&&')[0]],i=sp(i,a)
        elif ':\n' in a[i]:
            drev[a[i].lstrip().replace(':','&&',1).split('&&')[0]] ,i= ob(i, a)
        else:
            drev[a[i].lstrip().replace(':','&&',1).split('&&')[0]]=a[i].lstrip().split(':')[1]
            i += 1
    return drev


def pr_sl(sl:dict,pr=0,flag=1):

    ke = sl.keys()
    if flag:
        print(pr*' '+'{')
    for i in ke:
        ob = sl[i]
        if isinstance(ob,dict):
            print(pr*' '+i+': {')
            pr_sl(ob,pr+1,0)
            print(',') if i != list(ke)[-1]  else print('')
        elif isinstance(ob,list):
            print(pr * ' ' + i + ': [')
            pr_ls(ob,pr+1,0)
            print(',') if i != list(ke)[-1] else print('')
        else:
            print((pr+1)*' '+'''"'''+ i + '''"''' +':'+sl[i],end='') if sl[i].isdigit() else print((pr+1)*' '+'''"'''+ i + '''"''' +':'+'''"'''+sl[i]+'''"''',end='')
            print(',') if i != list(ke)[-1] else print('')
    print(pr*' '+'}',end='')
def pr_ls(sl:list,pr=0,flag =1):
    if flag:
        print(pr*' '+'[')
    for i in range(len(sl)):
        ob=sl[i]
        if isinstance(ob,dict):
            pr_sl(ob,pr+1)
            print(',') if i!=len(sl)-1 else print('')
        elif isinstance(ob,list):
            pr_ls(ob,pr+1)
            print(',') if i != len(sl) - 1 else print('')
        else:
            print((pr+1)*' '+ob,end='')
            print(',') if i != len(sl) - 1 else print('')
    print(pr*' '+']',end='')
def sdel_json(drev):
    pr_sl(drev)
