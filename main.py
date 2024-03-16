
import math, itertools, functools

convertCodeToNumber = {
  "55": 1,
  "BD": 2,
  "E9": 3,
  "7A": 4,
  "1C": 5,
  "FF": 6
}
convertNumberToCode = ["55", "BD", "E9", "7A", "1C", "FF"]

def translateSequence(arr):
  return [convertCodeToNumber[x] for x in arr]

inputBoard = ["55", "BD", "E9", "7A", "E9", "1C", "1C", "7A", "1C", "E9", "BD", "1C", "BD", "E9", "BD", "1C", "55", "BD", "BD", "55", "1C", "1C", "1C", "BD", "1C", "1C", "1C", "55", "55", "7A", "E9", "1C", "1C", "7A", "7A", "1C"]

translatedBoard = translateSequence(inputBoard)


def findAnsReq(board, targets):
  size = math.isqrt(len(board))

  def searchCol(line, path: list[int], subTarget):
    for x in range(size):
      pos = line + x*size
      if subTarget[0] != -1 and board[pos] != subTarget[0]: continue
      if pos in path: continue
      if len(subTarget) == 1:
        return path + [pos]
      validPath = searchRow(x, path + [pos], subTarget[1:])
      if validPath is not None:
        return validPath
    return None
  
  def searchRow(line, path, subTarget):
    for x in range(size):
      pos = line * size + x
      if subTarget[0] != -1 and board[pos] != subTarget[0]: continue
      if pos in path: continue
      if len(subTarget) == 1:
        return path + [pos]
      validPath = searchCol(x, path + [pos], subTarget[1:])
      if validPath is not None:
        return validPath
    return None

  for x in [functools.reduce(lambda a, b: a+b, x) for x in itertools.permutations(targets)]:
    a = searchRow(0, [], x)
    if a is not None:
      return a


sequences = [[3,5,5,1],[5,3,2,3,4]]

answer = findAnsReq(translatedBoard, sequences)

size = math.isqrt(len(translatedBoard))

print([(x % size, x // size) for x in answer])