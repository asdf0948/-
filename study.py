num_list = [] 
mod_list = []

for i in range(10):
    num_list.append(int(input()))

for i in num_list:
    mod = i % 42
    if mod in mod_list:
        pass
    else:
        mod_list.append(mod)

print(mod_list)