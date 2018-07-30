l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'a', 'a', 'a', 'a']
print("l1:%s l2:%s" % (id(l1), id(l2)))
l1, l2 = l2, l1
print("l1:%s l2:%s" % (id(l1), id(l2)))