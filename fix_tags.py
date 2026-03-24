 import json

with open('RF.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        if 'tags' not in cell['metadata']:
            cell['metadata']['tags'] = []
        if 'hide-input' not in cell['metadata']['tags']:
            cell['metadata']['tags'].append('hide-input')

with open('RF.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Pronto!')
