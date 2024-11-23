import numpy as np
from collections import Counter

POPULATION = 1000000


def experiment():
    ones = np.ones(int(.35 * POPULATION))
    neg_ones = np.full(int(.4 * POPULATION), -1)
    zeros = np.zeros(int(.25 * POPULATION))

    all_votes = np.concatenate((ones, neg_ones, zeros))
    np.random.shuffle(all_votes)

    sum_neg_one = 0

    for i in range(200):
        samp = np.random.choice(all_votes, 200)
        counts = Counter(samp)
        if counts.most_common(1)[0][0] == -1:
            sum_neg_one += 1

    return float(sum_neg_one) / 200


print(experiment())