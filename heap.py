from heapq import heappush
#using heappush
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

print("\n--___•___--___•___--___•___--___•___--___•___--\n")
#using heappop
from heapq import heappop

print(heappop(fruits))

print(fruits)

print("\n--___•___--___•___--___•___--___•___--___•___--\n")
#tuple comparison
person1 = ("Jez", "Berry", 42)
person2 = ("Jez", "Domer", 42)
person3 = ("Jez", "Domer", 24)

print(person1 < person2)

print(person2 < person3)
