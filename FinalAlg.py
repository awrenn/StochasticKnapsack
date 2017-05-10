import random
import time
import math
import pickle

class item:
    def __init__(self,min_v,max_v,min_w,max_w):
        self.max_v = max(max_v,min_v)
        self.min_v = min(max_v,min_v)
        self.max_w = max(max_w,min_w)
        self.min_w = min(max_w,min_w)
        self.exp_v = (max_v + min_v)/2.0
        self.exp_w = (max_w + min_w)/2.0

    def expected_return(self,remaining):
        range_w = self.max_w - self.min_w + 1
        allowed_w = remaining - self.min_w + 1
        possible_percent = float(allowed_w)/float(range_w)
        if possible_percent < 0:
            return 0
        else:
            return min(self.exp_v * possible_percent, self.exp_v)

    def get_score(self,remaining,lambdas):
        expected_return = self.expected_return(remaining)
        max_w = self.max_w
        min_w = self.min_w
        exp_v = self.exp_v
        exp_w = self.exp_w
        return (lambdas[0]*expected_return/float(exp_w) + lambdas[1]*(1/12.0*(max_w - min_w)**2) + lambdas[2]*(float(exp_v)))

def make_items(n,min_v,max_v,min_w,max_w):
    items = []
    for i in range(n):
        v = random.randint(min_v,max_v)
        V = random.randint(min_v,max_v)
        w = random.randint(min_w,max_w)
        W = random.randint(min_w,max_w)
        items += [item(v,V,w,W)]
    return items

def hify_make_items(items):
    weights = []
    values = []
    for new_item in items:
        weights += [int(math.ceil(new_item.exp_w))]
        values += [new_item.exp_v]
    return weights, values

def o_h_knapSack(W, items):
    #Currently most promising
    if len(items) == 0:
        return 0
    if W <= 0:
        return 0
    n = len(items)
    wt,val = hify_make_items(items)
    K = []
    print(W)
    p = [0 for x in range(W+1)]
    for z in range(n+1):
        K += [p[:]]
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
                pass
            item = items[i-1]
            attempt = 0
            to_use = [item.min_w,item.max_w]
            if item.exp_w % 1 == .5:
                to_use += [int(item.exp_w - .5), int(item.exp_w + .5)]
            else:
                to_use += [int(item.exp_w)]
            for wt in to_use:
                if wt <= w:
                    attempt += item.exp_v + K[i-1][w-wt]
            attempt /= int(item.max_w - item.min_w + 1)
            if attempt > K[i-1][w]:
                K[i][w] = attempt
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


def stoch_knapsack(weight,items,lambdas = [1,0,0]):
    items = sorted(items, key = lambda item: -item.get_score(weight,lambdas))
    if not items or weight <= 0:
        return 0
    total_max = 0
    for item in items:
        total_max += item.max_w
    weight = min(weight,total_max)
    possibilities = []
    for item in items:
        temp_items = items.copy()
        temp_items.remove(item)
        ev = 0
        to_use = [item.min_w,item.max_w]
        if item.exp_w % 1 == .5:
            to_use += [int(item.exp_w - .5), int(item.exp_w + .5)]
        else:
            to_use += [int(item.exp_w)]
        for wt in to_use:
            if wt <= weight:
                ev += item.exp_v + o_h_knapSack(weight-wt,list(temp_items))
        possibilities += [(ev/(item.max_w-item.min_w+1),item)]

    possibilities = sorted(possibilities, key = lambda x: -x[0])
    choice = possibilities.pop(0)[1]
    used_cost = random.randint(choice.min_w,choice.max_w)
    items.remove(choice)
    if used_cost > weight:
        return 0
    else:
        return (choice.exp_v + stoch_knapsack(weight-used_cost,items))
