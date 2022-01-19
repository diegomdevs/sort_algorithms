def selectionSort(array: list = [10, 9, 8, 7 ,6 , 5 ,4 ,3, 2, 1], wasChange: bool = False) -> list:
  """This method will sort a number array.

  Args:
      array (list, optional): unordered number array. Defaults to [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].
      wasChange (bool, optional): This conditional is to indicate that the cycle does not repeat itself unnecessarily more times. Defaults to False.

  Returns:
      list: sorted array.
  """
  for i in  range(len(array)):
    wasChange = False
    idxDes: int = i
    for j in range(i+1, len(array)):
      if array[idxDes] > array[j]:
        wasChange = True
        idxDes = j
      if wasChange == False:
        break
    array[i], array[idxDes] = array[idxDes], array[i]
  return array

def main() -> None:
  print(selectionSort(['b', 'c', 'a']))

if __name__ == "__main__":
  main()