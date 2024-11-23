import numpy as np
from collections import Counter

POPULATION = 1000000

np.random.seed(4321)

def experiment(num_samples):
    ones = np.ones(int(.35 * POPULATION))
    neg_ones = np.full(int(.4 * POPULATION), -1)
    zeros = np.zeros(int(.25 * POPULATION))

    all_votes = np.concatenate((ones, neg_ones, zeros))
    np.random.shuffle(all_votes)

    sum_neg_one = 0

    for i in range(200):
        samp = np.random.choice(all_votes, num_samples, replace=False)
        counts = Counter(samp)
        most_common = counts.most_common(1)[0]
        if counts.most_common(1)[0][0] == -1:
        # if most_common[0] == -1 and most_common[1] >= NUM_SAMPLES / 2:
            sum_neg_one += 1

    return float(sum_neg_one) / 200

print(experiment(10))
print(experiment(120))
print(experiment(250))