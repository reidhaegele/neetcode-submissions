class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        line = [0] * 1001

        for trip in trips:
            p, f, t = trip

            line[f] += p
            line[t] += -p
        
        curr = 0
        for people in line:
            curr += people
            if curr > capacity:
                return False
        
        return True
