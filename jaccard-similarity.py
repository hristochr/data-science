from math import*
 
def get_jaccard_similarity(x,y):
 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

print ('Similar sets:')
print(get_jaccard_similarity([1,2,3],[3,4,5])) #similar
print('--------------')
print ('Identical sets:')
print(get_jaccard_similarity(['d','b','c'],['b','c','d'])) # identical
print('--------------')
print ('Different sets:')
print(get_jaccard_similarity(['x','y','z'],['b','c','d'])) # different
print('--------------')
