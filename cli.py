import yaml
import sys

file_path = 'new_SOL.yaml'
sys.stdout = open(file_path, 'w')

with open('AllComponentsFromSOL.yaml', 'r') as origin:
    docs = yaml.safe_load_all(origin)
    for smth in docs:
        print(smth ['metadata'] ['name'])
#    sort_file = yaml.dump(smth ['metadata'], sort_keys=True)
#    print(sort_file)

