import FinalAlg as slow
import knapsack01 as quick
import pickle
import time
import random
import math

class item:
    def __init__(self,min_v,max_v,min_w,max_w):
        self.max_v = max(max_v,min_v)
        self.min_v = min(max_v,min_v)
        self.max_w = max(max_w,min_w)
        self.min_w = min(max_w,min_w)
        self.exp_v = (max_v + min_v)/2
        self.exp_w = (max_w + min_w)/2

    def expected_return(self,remaining):
        range_w = self.max_w - self.min_w + 1
        allowed_w = remaining - self.min_w + 1
        possible_percent = float(allowed_w)/float(range_w)
        if possible_percent < 0:
            return 0
        else:
            return min(self.exp_v * possible_percent, self.exp_v)

    def actual_weight(self):
        return random.randint(self.min_w, self.max_w)

    def actual_value(self):
        return self.exp_v

values_slow = []
values_quick = []
for i in range(10):
    weights, values, items = quick.make_items(99,2,10,2,10)
    for t in range(10):
        tic = time.time()
        a = slow.stoch_knapsack(120,items[:])
        toc = time.time()
        print(toc-tic)
        tic = time.time()
        b = quick.knapSack(120,weights,values,items[:])
        toc = time.time()
        print(toc-tic)
        values_slow += [a]
        values_quick += [b[0]]

with open("trick_items.txt","rb") as fp:
    items = pickle.load(fp)

weights, values = slow.hify_make_items(items)
for t in range(1):
    a = slow.stoch_knapsack(11,items[:])
    b = quick.knapSack(11,weights,values,items[:])
    print(a)
    print(b)

print(sum(values_slow)/len(values_slow))
print(sum(values_quick)/len(values_quick))
