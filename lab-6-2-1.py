def add_num(seq, num):
    seq = list(seq)
    for i in range(len(seq)):
        seq[i] = seq[i] + num
    return seq

def min_num(seq, num):
    seq = list(seq)
    for i in range(len(seq)):
        seq[i] = seq[i] + num
    return seq
 
origin = (0, 1, 2, 3 , 4)
changed = add_num(origin, 2)

msans = (0 , -1 , -2 , -3 , -4)
mchanged = min_num(msans , -2)


print(mchanged)
print(changed)

m = mchanged + changed
print(m)

x = m.count(0)
print(x)
