
import math

convertCodeToNumber = {
  "55": 1,
  "BD": 2,
  "E9": 3,
  "7A": 4,
  "1C": 5,
  "FF": 6
}
convertNumberToCode = ["", "55", "BD", "E9", "7A", "1C", "FF"]

def translateSequence(arr):
  return [convertCodeToNumber[x] for x in arr]

def findAnsReq(board, targets, bufferSize):
  size = math.isqrt(len(board))

  bestScore = (2**len(targets)-1)

  maxScore = 0
  maxPath = None

  def score(path: list[int]) -> int:
    s = 0
    full = "".join([str(board[x]) for x in path])
    for i, target in enumerate(targets):
      targetStr = "".join(map(str, target))
      if targetStr in full:
        s += 2**i
    return s

  def search(line, path: list[int]):
    nonlocal maxPath
    nonlocal maxScore
    for x in range(size):
      if len(path) % 2 == 0:
        pos = line * size + x
      else:
        pos = line + x*size
      if pos in path: continue
      nPath = path + [pos]
      if len(nPath) == bufferSize:
        nScore = score(nPath)
        if nScore > maxScore:
          maxScore = nScore
          maxPath = nPath
          if nScore == bestScore:
            return True
        return False
      terminate = search(x, nPath)
      if terminate:
        return True
    return False
  
  search(0,[])
  return maxPath

with open("board.txt","r") as f:
  boardText = f.read()

inputBoard = translateSequence(" ".join(boardText.split(" \n")).split(" "))

with open("sequences.txt", "r") as f:
  sequenceText = f.read()

sequences = [translateSequence(x.strip().split(" ")) for x in sequenceText.split("\n")]

bufferSize = 8

answer = findAnsReq(inputBoard, sequences, bufferSize)

size = math.isqrt(len(inputBoard))

print([(x % size, x // size) for x in answer])
print(answer)
print([convertNumberToCode[inputBoard[x]] for x in answer])


