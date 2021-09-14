import os
print(os.path.exists("F1.txt"))
print(os.path.getsize("F2.txt"))
f = open('F1.txt.', 'r')
def fun():
    with open('F1.txt') as f, open('F2.txt', 'w') as g:
        my_str = f.read().splitlines()
        res = []
        for st in my_str:
            if any((s.lower().startswith('a') for s in st)):
                res.append(st)
        if not res:
            res = ['0']
        g.write('\n'.join(res))
        print(res)
fun()