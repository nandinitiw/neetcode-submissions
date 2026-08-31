class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        
        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x<y:
                heapq.heappush(stones, -1*((-1*x)-(-1*y)))
            print(stones)

        if len(stones)==0:
            return 0
        return -1*stones[0]
        