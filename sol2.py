def sol2(st1):
    for i,c in enumerate(st1):
        if(st1.count(c) == 1):
            return i
    return -1

print("Example 1:",sol2("leetcode"))
print("Example 2:",sol2("loveleetcode"))
print("Example 3:",sol2("aabb"))
print("Example 4:",sol2("united nation secutity council"))