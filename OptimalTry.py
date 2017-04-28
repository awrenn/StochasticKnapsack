def o_h_knapSack(W, items):
    #Currently most promising
    n = len(items)
    wt,val = hify_make_items(items)
    K = [[[0,set(items)] for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w][0] = 0
                pass
            item = items[i-1]
            attempt = 0
            for wt in range(item.min_w,item.max_w+1):
                if wt <= w:
                    attempt += item.exp_v + K[i-1][w-wt][0]
            attempt /= int(item.max_w - item.min_w + 1)
            if attempt > K[i-1][w][0]:
                K[i][w][0] = attempt
            else:
                K[i][w][0] = K[i-1][w][0]
                K[i][w][1] = K[i-1][w][1]
                K[n][W][1].discard(item)
    return K[n][W][:]
