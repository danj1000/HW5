from random import random
import random as rand

rand.seed(8329)

p = 0.5

def experiment(t):
    counts = []
    for _ in range(50):
        s = [0]
        for i in range(t):
            r = random()
            diff = -1
            if r < p:
                diff = 1
            s.append(s[-1] + diff)

        count = 0
        for i in range(t-2):
            if s[i + 1] == 0:
                if s[i] < 0 < s[i + 2]:
                    count += 1
                elif s[i] > 0 > s[i + 2]:
                    count += 1

        counts.append(count)

    return sum(counts) / len(counts)

print(experiment(4*10**4))
print(experiment(9*10**4))
print(experiment(16*10**4))