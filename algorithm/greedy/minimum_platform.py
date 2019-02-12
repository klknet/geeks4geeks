"""
Minimum number of platforms required for a Railway Station
Given arrived and departed times of all trains that reach a Railway Station, find the minimum number of platforms required
for s railway station so that no trains wait
Solution:
sort the arrive and depart time, once we have all events in sorted order, we can trace the number of trains at any time
keeping track of trains that have arrived, but not departed.
"""


def required_platforms(arrive, depart):
    n = len(arrive)
    plat_required = 1  # at least 1 platform is needed
    result = 1
    i, j = 1, 0
    arrive.sort()
    depart.sort()
    while i < n and j < n:
        if arrive[i] > depart[j]:
            plat_required -= 1
            j += 1
        else:
            plat_required += 1
            i += 1
            if plat_required > result:
                result = plat_required
    return result


arrive = [900, 940, 950, 1100, 1500, 1800]
depart = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum number of platforms required is", required_platforms(arrive, depart))
