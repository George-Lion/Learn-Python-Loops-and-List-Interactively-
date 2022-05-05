arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_Odds():
    odds = []
    for value in arr:
        if value % 2 != 0:
            odds.append(value)
            total = sum(odds)
    return total
print(sum_Odds())
