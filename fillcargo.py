def loadTheCargo(num: int, containers: List[int], itemSize: int, itemsPerContainer: List[int], cargoSize: int) -> int:
    out = 0
    while cargoSize > 0 and itemsPerContainer:
        i = itemsPerContainer.index(max(itemsPerContainer))
        size = min(cargoSize, containers[i])
        out += size*itemsPerContainer[i]
        itemsPerContainer.pop(i)
        containers.pop(i)
        cargoSize -= size
    return out