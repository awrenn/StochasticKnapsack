import FinalAlg as slow
import learning_algorithm as greedy
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

    def get_score(self,remaining,lambdas):
        expected_return = self.expected_return(remaining)
        max_w = self.max_w
        min_w = self.min_w
        exp_v = self.exp_v
        exp_w = self.exp_w
        return (lambdas[0]*expected_return/float(exp_w) + lambdas[1]*(1/12.0*(max_w - min_w)**2)*expected_return + lambdas[2]*(float(exp_v)*expected_return))

    def actual_weight(self):
        return random.randint(self.min_w, self.max_w)

    def actual_value(self):
        return self.exp_v

def make_items_number_1():
    items = []
    values = []
    weights = []
    for i in range(99):
        new_item = item(20,20,2**100/20,2**100/20)
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    new_item = item(1000,1000,2**100,2**100)
    items += [new_item]
    values += [new_item.exp_v]
    weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_2():
    items = []
    values = []
    weights = []
    for i in range(99):
        new_item = item(20,20,2**100/20,2**100/20)
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    new_item = item(1000,1000,2**100+1,2**100+1)
    items += [new_item]
    values += [new_item.exp_v]
    weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_3():
    items = []
    values = []
    weights = []
    for i in range(10):
        new_item = item(1,1,1,1)
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    for i in range(10,100):
        new_item = item(1000,1000,2**100,2**100)
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_4():
    items = []
    values = []
    weights = []
    for i in range(1,101):
        new_item = item(2**100-2**(i-1),2**100+2**(i-1),2**94-2**(i-1),2**94+2**(i-1))
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_5():
    items = []
    values = []
    weights = []
    for i in range(1,101):
        new_item = item(1,100,2**94-2**(i-1),2**94+4**(i-1))
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_6():
    items = []
    values = []
    weights = []
    for i in range(1,101):
        new_item = item(0,2**i,2**94-2**(i-1),2**94+4**(i-1))
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    return weights, values, items

def make_items_number_7():
    items = []
    values = []
    weights = []
    for i in range(1,101):
        new_item = item(0,2**i,2**(i-1),2**i)
        items += [new_item]
        values += [new_item.exp_v]
        weights += [int(new_item.exp_w)]
    return weights, values, items

lambdas = [1,-0.01,0.01]
weights, values, items = make_items_number_1()
a = greedy.stoch_knapsack(items[:],2**100,lambdas)
print(a)

weights, values, items  = make_items_number_2()
a = greedy.stoch_knapsack(items[:],2**100,lambdas)
print(a)

weights, values, items  = make_items_number_3()
a = greedy.stoch_knapsack(items[:],2**100,lambdas)
print(a)

weights, values, items  = make_items_number_4()
vals = []
for t in range(100):
    vals += [greedy.stoch_knapsack(items[:],2**100,lambdas)]
print(sum(vals)/len(vals))

weights, values, items  = make_items_number_5()
vals = []
for t in range(100):
    vals += [greedy.stoch_knapsack(items[:],2**100,lambdas)]
print(sum(vals)/len(vals))

weights, values, items  = make_items_number_6()
vals = []
for t in range(100):
    vals += [greedy.stoch_knapsack(items[:],2**100,lambdas)]
print(sum(vals)/len(vals))

weights, values, items  = make_items_number_7()
vals = []
for t in range(100):
    vals += [greedy.stoch_knapsack(items[:],2**100,lambdas)]
print(sum(vals)/len(vals))


#print(sum(values_slow)/len(values_slow))
#print(sum(values_quick)/len(values_quick))
