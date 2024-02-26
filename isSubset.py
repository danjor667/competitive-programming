def isSubset( a1, a2, n, m):
    from collections import Counter
    
    my_dict = Counter(a1)
    for ele in a2:
        rest = my_dict.get(ele, 0)  - 1
        my_dict[ele] = rest
        if rest < 0:
            return "No"
    return "Yes"
