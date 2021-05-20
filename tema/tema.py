# Ex 1
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Ex 2
ascending_list = list.copy()
ascending_list.sort()

print("Exercitiul 2")
print(list)
print(ascending_list)

# Ex 3
descending_list = list.copy()
descending_list.sort(reverse=True)

print("Exercitiul 3")
print(descending_list)

# Ex 4
odd_list = []
even_list = []

print("Exercitiul 4")
for i in list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(odd_list)
print(even_list)

# Ex 5
new_list = []

print("Exercitiul 5")
for i in list:
    if i % 3 == 0:
        new_list.append(i)

print(new_list)
