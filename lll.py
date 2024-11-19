import json
import yaml
import time
import main
import pppr
import pr
p1 = time.time()
with open('Lol.yml', encoding='utf-8') as ll:
    for i in range(100):
        yamlobj = yaml.load(ll, Loader=yaml.FullLoader)
        json.dumps(yamlobj, indent=4, sort_keys=False, ensure_ascii=False)
    print(time.time()-p1)
a = open('Lol.yml', encoding="utf-8").readlines()
json.dumps(yamlobj,indent=4, sort_keys=False, ensure_ascii=False)
p1 = time.time()
for i in range(100):
    b=a.copy()
    main.st(b)
print(time.time()-p1)

p1 = time.time()
for i in range(100):
    pppr.sdel_json(pppr.star(a))
print(time.time()-p1)
p1 = time.time()
for i in range(100):
    pr.str(a)
print(time.time()-p1)