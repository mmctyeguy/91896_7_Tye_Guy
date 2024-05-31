binary = [0, 1, 1, 0, 0, 0]
decimal = [32, 16, 8, 4, 2, 1]
output_decimal = []

for i, b in enumerate(binary):
    if b != 0:
        output_decimal.append(decimal[i])

print(output_decimal)
