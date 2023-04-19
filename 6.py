
def sum_of_squares():
    squares = []
    for i in range(100):
        squares.append(int((i+1)**2))
    return sum(squares)

def square_of_sum():
    nums = []
    for i in range(100):
        nums.append(i+1)
    return (sum(nums))**2

print(square_of_sum()-sum_of_squares())