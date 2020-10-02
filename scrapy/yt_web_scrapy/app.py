import collections
s = set()
arr = [2, 2, 3, 4, 5, 1,4]
# dupli=[el for el in arr if el not ]
res = collections.Counter(arr).items()
uniq = [ele for ele, count in res if count > 1]
print(uniq)
