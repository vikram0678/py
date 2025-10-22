def numJewelsInStones(jewels, stones):
    jset = set(jewels)
    count = 0
    for s in stones:
        if s in jset:
            count += 1
    return count
jewels = "aA", stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))  # Output: 3
 
