def partitionString(input):
    """
    :type input: str
    :rtype: List[str]
    """
    last = {}
    for i,c in enumerate(input):
        last[c] = i
    out = []
    current = ''
    right = last[input[0]]
    ch = input[0]
    for i,c in enumerate(input):
        current += c
        right = max(right,last[c])
        if i == right:
            out.append(current)
            current = ''
            right = right+1
    if len(current) > 0:
        out.append(current)
    return out