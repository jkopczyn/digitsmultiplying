import itertools

def gen_foursets(iterable):
    return itertools.combinations(iterable, 4)

def fourset_permutations(fourset):
    return itertools.permutations(fourset)

def random_product(fourlist):
    a,b,c,d = fourlist
    return (10*a+b) * (10*c+d)

def clever_product(fourlist, full_list):
    fourlist = list(fourlist)
    total = sum(full_list)
    l = len(full_list)
    a=b=c=d=None
    temp = fourlist.pop()
    total -= temp
    l -= 1
    if temp <= total/l:
        a = temp
        temp = fourlist.pop()
        total -= temp
        l -= 1
        if temp <= total/l:
            c = temp
            temp = fourlist.pop()
            total -= temp
            l -= 1
            #this is xor
            if set([temp <= total/l, c < a]) == set([True, False]):
                d = temp
                b = fourlist.pop()
            else:
                b = temp
                d = fourlist.pop()
        elif temp <= 1.5*total/l:
            b = temp
            temp = fourlist.pop()
            total -= temp
            l -= 1
            if temp <= total/l:
                c = temp
                d = fourlist.pop()
            else:
                d = temp
                c = fourlist.pop()
        else:
            d = temp
            temp = fourlist.pop()
            total -= temp
            l -= 1
            if temp <= total/l:
                c = temp
                b = fourlist.pop()
            else:
                b = temp
                c = fourlist.pop()
    else:
        b = temp
        #placeholder
        a,c,d = fourlist
    print a, b, c, d
    return random_product([a,b,c,d])


def optimal_product(fourlist):
    return min((random_product(f) for f in fourset_permutations(fourlist)))

full = list(range(10))
sets = gen_foursets(full)
permutations = (fourset_permutations(p) for p in sets)
print [clever_product(l, full) for plist in permutations for l in plist]
