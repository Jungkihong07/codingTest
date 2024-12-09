location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2),
         (-1, -2)]

result = 0
for i in steps:
  next_row = row + i[0]
  next_column = column + i[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
