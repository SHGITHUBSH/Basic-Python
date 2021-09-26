# Can combine two data set, or to pick the mutual data sets, mutable
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
series = {2,3,8,9}

u =odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

diff = odds.difference(evens)
print(diff)

diff1 = primes.symmetric_difference(evens)
print(diff1)

primes.update(evens)
print(primes)

primes.intersection_update(series)
print(primes)

#Fronzen set, once create, it doesn't let you modify it
a = frozenset([1,2,3,4])
a.add(2)
a.remove(2)
a.update(5)
print(a)
#As you can see, it won't work since fronzen set is immutable