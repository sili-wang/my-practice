#If no cities found, return None instread of string "None"
def findNearestCities(numOfPoints: int, points: List[str], xCoordinates: List[int], yCoordinates: List[int],
                      numOfQueriedPoints: int, queriedPoints: List[str]) -> List[str]:
                          out = []
                          for point in queriedPoints:
                              heap = []
                              i = points.index(point)
                              x = xCoordinates[i]
                              y = yCoordinates[i]
                              for j in range(len(points)):
                                  if j == i:
                                      continue
                                  else:
                                      if x == xCoordinates[j] or y == yCoordinates[j]:
                                          heapq.heappush(heap,(abs(x-xCoordinates[j])+abs(y-yCoordinates[j]),points[j]))
                              if not heap:
                                  out.append(None)
                              else:
                                  dif, name = heapq.heappop(heap)
                                  print(name)
                                  out.append(name)
                          return out