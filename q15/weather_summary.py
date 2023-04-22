def weatherSummaryOne(isRaining, temp):
    if isRaining:
        if temp < 15:
            print("It's wet and cold")
        else:
            print("It's warm and raining")
    else:
        if temp < 15:
            print("It's not raining but cold")
        else:
            print("It's warm but not raining")



def weatherSummaryTwo(isRaining, temp):
    if isRaining and temp < 15:
        print("It's wet and cold")
    elif isRaining and temp >= 15:
        print("It's warm and raining")
    elif not isRaining and temp < 15:
        print("It's not raining but cold")
    else:
        print("It's warm but not raining")


# weatherSummary(True, 14)

# celsius = float(input())

# farehnheit = (celsius*9/5)+32

# print(f"The result is: {farehnheit}.")

arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

i = 0

while (i < len(arr) -1) and (arr[i] < arr[i+1]):
    i += 1
print(i)
indexCache = arr[i]
arr[i] = arr[i+1]
arr[i+1] = indexCache



print(arr)


