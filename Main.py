from typing import List

def selectionSort(array, size) -> List[int]:
  for index in range(size):
    min_index = index
    for ind in range(index + 1, size):
      if array[ind] < array[min_index]:
        min_index = ind
    array[min_index], arrray[index] = array[index], array[min_index]
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
