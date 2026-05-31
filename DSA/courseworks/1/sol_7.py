import math

def successfulPairs(spells, potions, success):
    potions.sort()
    n = len(spells)
    m = len(potions)
    pairs = []
    
    for spell in spells:
        target = math.ceil(success / spell)
        
        left, right = 0, m - 1
        index = m
        
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] >= target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
                
        pairs.append(m - index)
        
    return pairs

spells1 = [5, 1, 3]
potions1 = [1, 2, 3, 4, 5]
success1 = 7
print(successfulPairs(spells1, potions1, success1))

spells2 = [3, 1, 2]
potions2 = [8, 5, 8]
success2 = 16
print(successfulPairs(spells2, potions2, success2))