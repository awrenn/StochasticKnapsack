import random
import time
import math

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

def stoch_knapsack(items,weight,lambdas):
    if weight == 0:
        return 0
    if not items:
        return 0

    items = sorted(items, key = lambda item: -item.get_score(weight,lambdas))
    selected = items.pop(0)
    value = selected.exp_v
    used_cost = random.randint(selected.min_w,selected.max_w)
    if used_cost > weight:
        return 0
    else:
        return (value + stoch_knapsack(items,weight-used_cost,lambdas))

def hify_make_items(items):
    weights = []
    values = []
    for new_item in items:
        weights.append(int(math.ceil(new_item.exp_w)))
        values.append(new_item.exp_v)
    return weights, values

# Returns the maximum value that can be put in a knapsack of capacity W
# using a Dynamic Programming approach
# Takes the capacity of the knapsack W, the list of weights, and the list
# of values
def o_h_knapSack(W, items):
    #Currently most promising
    n = len(items)
    wt,val = hify_make_items(items)
    K = []
    used_items = []
    p = [0 for x in range(W+1)]
    for z in range(n+1):
        K += [p[:]]
        used_items += [p[:]]

    # Build table K[][] in bottom up manner
    for i in range(1,n+1):
        for w in range(1,W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
                pass
            item = items[i-1]
            attempt = 0
            for wt in range(item.min_w,item.max_w+1):
                if wt <= w:
                    attempt += item.exp_v + K[i-1][w-wt]
            attempt /= int(item.max_w - item.min_w + 1)
            if attempt > K[i-1][w]:
                K[i][w] = attempt
                used_items[i][w] = 1
            else:
                K[i][w] = K[i-1][w]
                used_items[i][w] = 0

    for w in range(W,-1,-1):
        for i in range(n,0,-1):
            if used_items[i][w] == 1:
                return(K[n][W],items[i-1])
    return None, None


def knapSack(W, items):
    #Currently most promising
    n = len(items)
    wt,val = hify_make_items(items)
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
                pass
            item = items[i-1]
            attempt = 0
            for wt in range(item.min_w,item.max_w+1):
                if wt <= w:
                    attempt += item.exp_v + K[i-1][w-wt]
            attempt /= int(item.max_w - item.min_w + 1)
            if attempt > K[i-1][w]:
                K[i][w] = attempt
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

def o_stoch_knapsack(weight,items,lambdas):
    total_max = 0
    for item in items:
        total_max += item.max_w
    weight = min(weight,total_max)
    possibilities = []
    for item in items:
        temp_items = items[:]
        temp_items.remove(item)
        for wt in range(item.min_w,item.max_w+1):
            val, selected = o_h_knapSack(weight,temp_items)
            possibilities += [(val+item.exp_v,selected)]

    possibilities = sorted(possibilities)
    choice = possibilities.pop(0)[1]
    used_cost = random.randint(choice.min_w,choice.max_w)
    items.remove(choice)
    if used_cost > weight:
        return 0
    else:
        return (choice.value + o_stoch_knapsack(weight-used_cost,items,lambdas))

for r in range(1):
    #random.seed(r)
    items = make_items(100,1,10,2,10)
    values = []
    values_2 = []
    lambdas = [1,0,0]
    for t in range(100):
        a = stoch_knapsack(items[:],120,lambdas)
        c = o_stoch_knapsack(120,items[:],lambdas)
        values += [a]
        values_2 += [c]
    print("Adjusted ratio:   ", sum(values)/float(len(values)), " on seed ", r)
    print("Expected Det:     ", sum(values_2)/float(len(values_2)), " on seed ", r)
    print('\n')

#print(stoch_knapsack(items,100000,lambdas))
