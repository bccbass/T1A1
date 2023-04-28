# def weatherSummaryOne(isRaining, temp):
#     if isRaining:
#         if temp < 15:
#             print("It's wet and cold")
#         else:
#             print("It's warm and raining")
#     else:
#         if temp < 15:
#             print("It's not raining but cold")
#         else:
#             print("It's warm but not raining")



def weatherSummaryTwo(isRaining, temp):
    if isRaining and temp < 15:
        print("It's wet and cold")
    elif isRaining and temp >= 15:
        print("It's warm and raining")
    elif not isRaining and temp < 15:
        print("It's not raining but cold")
    else:
        print("It's warm but not raining")

weatherSummaryTwo(False, 14)
# weatherSummary(True, 14)

# celsius = float(input())

# farehnheit = (celsius*9/5)+32

# print(f"The result is: {farehnheit}.")
