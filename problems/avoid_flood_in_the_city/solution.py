class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [-1] * n
        drydays = []
        full_lakes = {}
        for i in range(n):
            if rains[i] > 0:
                lake = rains[i]
                if lake in full_lakes:
                    found = False
                    for j in range(len(drydays)):
                        if drydays[j] > full_lakes[lake]:
                            result[drydays[j]] = lake
                            drydays.pop(j)
                            found = True
                            break
                    if not found:
                        return []
                full_lakes[lake] = i
            else:
                drydays.append(i)
        for i in drydays:
            result[i] = 1
        return result
