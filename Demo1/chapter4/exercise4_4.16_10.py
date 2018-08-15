import random
num_list = [chr(random.randint(48, 57)) for i in range(3)]
a_list = [chr(random.randint(97, 122)) for i in range(3)]
A_list = [chr(random.randint(65, 90)) for i in range(3)]
s = []
s.append(random.choice(num_list))
s.append(random.choice(a_list))
s.append(random.choice(A_list))
code_list = []
code_list.extend(num_list)
code_list.extend(a_list)
code_list.extend(A_list)
if code_list:
    l1 = random.sample(code_list, 3)
    s.extend(l1)
random.shuffle(s)
print(''.join(s))