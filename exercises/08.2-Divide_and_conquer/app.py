list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(array):

    odd_and_even = []
    odd = []
    even = []

    for i in array:
        if i %2 == 0:
            odd.append(i)
        
        elif i %2 == 1:
            even.append(i)

        odd_and_even = [even] +  [odd] 

    return odd_and_even

print(merge_two_list(list_of_numbers))

