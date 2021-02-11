def fiveStartReviews(productRatings, ratingsThreshold):
    out = 0
    heap = []
    l = len(productRatings)
    avgrate = 0
    for i in range(l):
        dif = productRatings[i][0] / productRatings[i][1] - (productRatings[i][0] + 1) / (productRatings[i][1] + 1)
        avgrate += productRatings[i][0] / productRatings[i][1]
        heapq.heappush(heap, (dif, i))

    avgrate = avgrate / l
    while avgrate < ratingsThreshold / 100:
        dif, i = heapq.heappop(heap)
        out += 1
        avgrate = (avgrate * l - dif) / l
        productRatings[i][0] += 1
        productRatings[i][1] += 1
        dif = productRatings[i][0] / productRatings[i][1] - (productRatings[i][0] + 1) / (productRatings[i][1] + 1)
        heapq.heappush(heap, (dif, i))
    return out