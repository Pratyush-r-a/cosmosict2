numbers=[4,7,10,13,18,21]
total_even=0
total_odd= 0
def check_odd_even(n):
    """check if a number is even or odd.  """
    if number%2 ==0:
        return "even"
    else:
        return "odd"
for number in numbers:
    if check_odd_even(number) == "even":
     total_even += 1
    else:
       total_odd += 1
print("total even numbers:", total_even)
print("total odd numbers:" ,total_odd)