class Calculator:
    def stand_dev(self, nums):
        mean = 0
        sumsq = 0
        for i in nums:
            mean+=i
            sumsq+=(i**2)
        mean/=len(nums)
        mean=mean**2
        stand = 0
        sumsq/=len(nums)
        stand=sumsq-mean
        stand=stand**(0.5)
        return(stand)
nums = [67, 102, 150]
y_val = [1, 2, 3]
num = []
stands = []
slope = []
c = Calculator()
for i in range(-100, 100):
    num = []
    for x in range(0, len(nums)):
        num.append(y_val[x]*(i))
        num[x] = nums[x]-num[x]
    slope.append(i)
    stands.append(c.stand_dev(num))
mini = min(stands)
for i in range(0, len(stands)):
    if stands[i] == mini:
        bestslope = slope[i]
        beststands = stands[i]
avy = 0
for i in range(0, len(nums)):
    avy+=(nums[i] - bestslope*(i+1))
avy/=len(nums)
print("Slope: " + str(bestslope))
print("Y-Int: " + str(avy))
print("Standard Deviation: " + str(beststands))
