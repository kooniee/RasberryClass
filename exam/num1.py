
nums = list({273, 103, 5, 32, 65, 72, 800, 99})

def printOdd(nums):
  for x in nums:
    if x % 2 == 1:
      print(x)

def printEven(nums):
  for x in nums:
    if x % 2 == 0:
      print(x)

print("짝수의 합 :")
printEven(nums)
print()
print("홀수의 합 :")
printOdd(nums)

