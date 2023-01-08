from collections import defaultdict

new_defaultdict = defaultdict(int)

print(new_defaultdict[5])

new_defaultdict_set = defaultdict(set)

new_defaultdict_set['One'].add(5)
new_defaultdict_set['Ten'].add(45)
new_defaultdict_set['Five'].add('15')
new_defaultdict_set['Ten'].add('17')
new_defaultdict_set['One'].add(8)
new_defaultdict_set['Five'].add('98')
new_defaultdict_set['Seven']

print(dict(new_defaultdict_set))
print(dict(new_defaultdict_set.items()))

new_defaultdict_set = defaultdict(list)

new_defaultdict_set['One'].append(5)
new_defaultdict_set['Ten'].append(45)
new_defaultdict_set['Five'].append('15')
new_defaultdict_set['Ten'].append('17')
new_defaultdict_set['One'].append(8)
new_defaultdict_set['Five'].append('98')
new_defaultdict_set['Seven']

print(dict(new_defaultdict_set))
print(dict(new_defaultdict_set.items()))

