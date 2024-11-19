import re
a = open('Lol.yml').readlines()
d=[]
for i in a:
    f=re.findall(r'([^-]+: .+)',i)[0].lstrip().split(':') if len(re.findall(r'([^-]+: .+)',i))>0 else ''
    if len(f)>0:
        d.append(f)

g=[]
for i in d:
    if i[0]!='предмет':
        g[-1].append(i[1].lstrip())
    else:
        g.append([i[1].lstrip()])
g=[['''"'''+j+'''"''' for j in i]for i in g]
ke = []
for i in d:
    if i[0] not in ke: ke.append(i[0])
ke = ['''"'''+i+ '''"''' for i in ke]
print(','.join(ke))
for i in g:
    print(','.join(i))
