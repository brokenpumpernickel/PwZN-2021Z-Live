from collections import defaultdict

x = {'karol': 5, 'renata': 9}
print(x)

print(f"{x['karol'] = }")
print(f"{x['renata'] = }")
x['bozydar'] = 289
print(f'{x = }')
del x['bozydar']
print(f'{x = }')
#print(f"{x['bozydar'] = }")

print(f'{"bozydar" in x = }')
print(f'{"renata" in x = }')
print(f'{"bozydar" not in x = }')

for e in x:
    print(f'{e = } {x[e] = }')

for e in x.keys():
    print(f'{e = } {x[e] = }')

for e in x.values():
    print(f'{e = }')

for e in x.items():
    print(f'{e = }')

for k, v in x.items():
    print(f'{k = } {v = }')

x = {i: i * i for i in range(10)}
print(x)

x = int()
print(x)

x = defaultdict(int)
x['bozydar'] += 1
print(x['bozydar'])