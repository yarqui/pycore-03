import random

def get_numbers_ticket(min, max, quantity):
    l = list()
    if min<1 or max>1000 or ((max - min) < quantity):
        return l
    

    nums = range(min,max)
    l = sorted(random.sample(nums, k=quantity))
    return l

# winners = get_numbers_ticket(1,100, 5)
winners = get_numbers_ticket(10, 12, 11)
print(winners)
