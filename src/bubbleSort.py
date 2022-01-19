def bubbleSort(array: list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], wasChange: bool = False) -> list:
  """This method will sort a number array.

  Args:
      array (list, optional): unordered number array. Defaults to [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].
      wasChange (bool, optional): This conditional is to indicate that the cycle does not repeat itself unnecessarily more times. Defaults to False.

  Returns:
      list: sorted array.
  """
  for i in range(len(array)):
    wasChange = False
    for j in range(0, len(array)-1):
      if array[j] > array[j + 1]:
        array[j], array[j+1] = array[j+1], array[j]
        wasChange = True
    if wasChange == False:
      return array

def main() -> None:
  print(bubbleSort([2,1]))
  return None
if __name__ == "__main__":
  main()