class SparseVector:
    def __init__(self, nums):
        self.map = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.map[i] = val

    def dotProduct(self, vec):
        result = 0
        
        # Iterate over smaller map (optimization)
        if len(self.map) < len(vec.map):
            for i in self.map:
                if i in vec.map:
                    result += self.map[i] * vec.map[i]
        else:
            for i in vec.map:
                if i in self.map:
                    result += self.map[i] * vec.map[i]
        
        return result


nums1 = list(map(int, input("Enter vector 1: ").split()))
nums2 = list(map(int, input("Enter vector 2: ").split()))

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print("Dot Product:", v1.dotProduct(v2))