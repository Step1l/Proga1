import json
import yaml
with open('Lol.yml', encoding='utf-8') as ll:
    yamlobj = yaml.load(ll, Loader=yaml.FullLoader)

print(json.dumps(yamlobj,indent=4, sort_keys=False, ensure_ascii=False))