import heapq
def maxprofit(arr,k):
    out = 0
    heap = []
    for i in arr:
        heapq.heappush(heap,-i)
    #heapq.heapify(arr)
    #print(heap)
    for i in range(k):
        p = heapq.heappop(heap)
        #print(arr)
        out -= p
        p += 1
        heapq.heappush(heap,p)
    return out

print(maxprofit([3,5,7,10,6],20))