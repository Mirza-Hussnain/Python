# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding elements to a set
set1.add(6)
set2.add(9)

# Removing elements from a set
set1.remove(3)
set2.discard(7)

# Union of sets
union_set = set1.union(set2)

# Intersection of sets
intersection_set = set1.intersection(set2)

# Difference of sets
difference_set = set1.difference(set2)

# Checking for subset
is_subset = set1.issubset(set2)

# Checking for superset
is_superset = set2.issuperset(set1)

# Displaying results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set (Set1 - Set2):", difference_set)
print("Is Set1 a subset of Set2?", is_subset)
print("Is Set2 a superset of Set1?", is_superset)
