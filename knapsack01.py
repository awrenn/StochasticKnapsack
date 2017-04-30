import random

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
        return random.randint(self.min_v, self.max_v)
        

def make_items(n,min_v,max_v,min_w,max_w):
    weights = []
    values = []
    items = []
    
    for i in range(n):
        v = random.randint(min_v,max_v)
        V = random.randint(min_v,max_v)
        w = random.randint(min_w,max_w)
        W = random.randint(min_w,max_w)
        new_item = item(v,V,w,W)
        items.append(new_item)
        weights.append(new_item.exp_w)
        values.append(new_item.exp_v)
                 
    return [weights, values, items]

# Returns the maximum value that can be put in a knapsack of capacity W
# using a Dynamic Programming approach
# Takes the capacity of the knapsack W, the list of weights, and the list
# of values
def knapSack(W, wt, val, items):
    n = len(val) 
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    value = 0
    
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    left = W #remaining space/weight in knapsack
    game_over = 0
    
    for j in range(n, 0, -1):
        was_added = K[j][left] != K[j-1][left]
 
        if was_added and game_over == 0:
            item_picked = items[j-1]
            wt = item_picked.actual_weight()
            if wt <= left:
                value += item_picked.actual_value()
                left -= wt
            else:
                game_over = 1
 
    return value, left

items = make_items(99,1,10,1,10)
#best_value = 0
acc_w = 0
    
best_value = knapSack(100, items[0], items[1], items[2])

    
    
    

print(best_value)


