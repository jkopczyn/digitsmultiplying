import itertools

def gen_foursets(iterable):
    return itertools.combinations(iterable, 4)

def fourset_permutations(fourset):
    return list(itertools.permutations(fourset))

def random_product(fourlist):
    a,b,c,d = fourlist
    return (10*a+b) * (10*c+d)

def percentian(item, lst, QUARTILE=0.25):
    place = next((i for i,v in enumerate(lst) if v >= item),
            len(lst)) * 1.0/len(lst)
    #0,1,2,3 => 'quartile', split by median and then by QUARTILEs away from med.
    if place < 0.5-QUARTILE:
        return 0
    elif place < 0.5:
        return 1
    elif place < 0.5+QUARTILE:
        return 2
    else:
        return 3


def clever_product(fourlist, full_list, QUARTILE=0.25):
    full_list = full_list[:]
    fourlist = list(fourlist)
    temp = fourlist.pop()
    full_list.remove(temp)
    if percentian(temp, full_list, QUARTILE) in [0,1]:
        a = temp
        temp = fourlist.pop()
        full_list.remove(temp)
        if percentian(temp, full_list, QUARTILE) in [0,1]:
            c = temp
            temp = fourlist.pop()
            full_list.remove(temp)
            #this is xor
            if set([percentian(temp, full_list, QUARTILE) in [0,1], c < a]) == set([True, False]):
                d = temp
                b = fourlist.pop()
            else:
                b = temp
                d = fourlist.pop()
        elif percentian(temp, full_list, QUARTILE) == 2:
            b = temp
            temp = fourlist.pop()
            full_list.remove(temp)
            if percentian(temp, full_list, QUARTILE) in [0,1]:
                c = temp
                d = fourlist.pop()
            else:
                d = temp
                c = fourlist.pop()
        else:
            d = temp
            temp = fourlist.pop()
            full_list.remove(temp)
            if percentian(temp, full_list, QUARTILE) in [0,1]:
                c = temp
                b = fourlist.pop()
            else:
                b = temp
                c = fourlist.pop()
    else:
        b = temp
        temp = fourlist.pop()
        full_list.remove(temp)
        if percentian(temp, full_list, QUARTILE) in [0,1]:
            if percentian(temp, full_list, QUARTILE) == 1:
                c = temp
                temp = fourlist.pop()
                full_list.remove(temp)
                if percentian(temp, full_list, QUARTILE) in [0,1]:
                    a = temp
                    d = fourlist.pop()
                else:
                    d = temp
                    a = fourlist.pop()
            else:
                a = temp
                temp = fourlist.pop()
                full_list.remove(temp)
                if percentian(temp, full_list, QUARTILE) in [0,1]:
                    c = temp
                    d = fourlist.pop()
                else:
                    d = temp
                    c = fourlist.pop()
        else:
            d = temp
            temp = fourlist.pop()
            full_list.remove(temp)
            #this is xor
            if set([percentian(temp, full_list, QUARTILE) in [0,1], d < b]) == set([True, False]):
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
