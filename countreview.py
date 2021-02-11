def countReview(lengths, minReviews, minLength, maxLength):
    qReview = 0
    out = 0
    for r in lengths:
        if r >= minLength and r <= maxLength:
            qReview += 1
    if qReview < minReviews:
        return 0
    else:

        for i in range(minReviews,qReview+1):
            q = 1
            s = 1
            for j in range(i):
                q = q*(qReview-j)
                s = s*(i-j)
            out += q/s
    return out

print(countReview([6,13,5,10,12,4,2,15], 3, 4, 10))

