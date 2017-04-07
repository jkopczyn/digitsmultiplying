import itertools

def gen_foursets(iterable):
    return itertools.combinations(iterable, 4)

def fourset_permutations(fourset):
    return list(itertools.permutations(fourset))

def random_product(fourlist):
    a,b,c,d = fourlist
    return (10*a+b) * (10*c+d)

def clever_product(fourlist, full_list, QUARTILE=0.5):
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
        elif temp <= (1 + QUARTILE)*total/l:
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
        temp = fourlist.pop()
        total -= temp
        l -= 1
        if temp <= total/l:
            if temp <= (1 - QUARTILE)*total/l:
                c = temp
                temp = fourlist.pop()
                total -= temp
                l -= 1
                if temp <= total/l:
                    a = temp
                    d = fourlist.pop()
                else:
                    d = temp
                    a = fourlist.pop()
            else:
                a = temp
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
            #this is xor
            if set([temp <= total/l, d < b]) == set([True, False]):
                a = temp
                c = fourlist.pop()
            else:
                c = temp
                a = fourlist.pop()
    return random_product([a,b,c,d])


def optimal_product(fourlist):
    return min((random_product(f) for f in fourset_permutations(fourlist)))

full = list(range(10))
sets = list(gen_foursets(full))
permutations = list(fourset_permutations(p) for p in sets)
clever_products = [clever_product(l, full) for plist in permutations for l in plist]
optimal_products = [optimal_product(l) for plist in permutations for l in plist]
random_products = [random_product(l) for plist in permutations for l in plist]
clever_sum = sum(clever_products)
random_sum = sum(random_products)
optimal_sum = sum(optimal_products)

print random_sum, clever_sum, optimal_sum
print [1, 1.0*clever_sum/random_sum, 1.0*optimal_sum/random_sum]
print ""

print [sum(clever_product(l, full, q/10.0) for plist in permutations for l in plist)
        for q in range(1,10)]
