from fprintx import printx


def check(n, h):
    x = set(h)
    if len(x) == 1 and 0 in x:
        return 'NO'
    elif sorted(h) == h and h[-1] > 0:
        return 'YES'
        

    prev_sum = 0    
    stack = []

    if h[0] > 0:
        stack.append(h[0]-1)
        prev_sum += 1
    else:
        stack.append(h[0])

    for i in range(1, n):
        if (h[i] + prev_sum) <= stack[-1]:
            return 'NO'
        
        if (h[i] + prev_sum)-1 > stack[-1]:
            stack.append((h[i]+prev_sum)-1)
            prev_sum += 1

        else:
            stack.append((h[i]+prev_sum))
            # prev_sum = max(0, prev_sum - 1)
    
    # print(*stack)
    return 'YES'



def check(n, h):
    running_val_sum = running_idx_sum = 0
    for i in range(n):
        running_idx_sum += i
        running_val_sum += h[i]
        if running_val_sum < running_idx_sum:
            return 'NO'
    return 'YES'
            


t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(check(n, h))



# Increasing sums of values and increasing sums of indices.