from random import randint

def create_array(size = 1000, max = 1000):
    return [randint(0, max) for _ in range(size)]

def quicksort(a):
    if len(a) <= 1:
        return a
    small, equal, large = [], [], []
    pivot = a[randint(0, len(a) - 1)]

    for x in a:
        if x < pivot:
            small.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            large.append(x)

    return quicksort(small) + equal + quicksort(large)

a = create_array()
print 'unsorted: ', a
s = quicksort(a)
print 'sorted: ', s
