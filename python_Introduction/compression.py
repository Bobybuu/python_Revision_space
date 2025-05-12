result = []
for x in range(10):
    for y in range(5):
        if x + y > 5:
            result.append(x * y)
print(result)

# Complex list comprehension (less readable)
result = [x * y for x in range(10) for y in range(5) if x + y > 5]