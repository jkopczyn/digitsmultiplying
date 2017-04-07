import itertools

def gen_foursets(iterable):
    return itertools.combinations(iterable, 4)

def fourset_permutations(fourset):
    return itertools.permutations(fourset)

def random_product(fourlist):
    a,b,c,d = fourlist
    return (10*a+b) * (10*c+d)

def clever_product(fourlist, total):
    pass

def optimal_product(fourlist):
    return min((random_product(f) for f in fourset_permutations(fourlist)))
