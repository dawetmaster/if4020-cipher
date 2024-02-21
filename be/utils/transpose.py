def transpose_bytes(bytes, colNum):
  # convert bytes to 2D array with colNum columns
  arr = [bytes[i:i+colNum] for i in range(0, len(bytes), colNum)]
  # pad the last row with b'x\00' if necessary
  if len(arr[-1]) < colNum:
    arr[-1] += b'x\00' * (colNum - len(arr[-1]))
  # transpose the 2D array
  arr_transposed = []
  for i in range(colNum):
    for j in range(len(arr)):
      if i < len(arr[j]):
        if i >= len(arr_transposed):
          arr_transposed.append(bytearray())
        arr_transposed[i].append(arr[j][i])
  # read the result vertically as a byte string
  result = b''.join(arr_transposed[i] for i in range(colNum))
  return result

def transpose_back_bytes(bytes, colNum):
  # calculate the number of rows
  rowNum = len(bytes) // colNum
  # convert bytes to 2D array with rowNum rows
  arr = [bytes[i:i+rowNum] for i in range(0, len(bytes), rowNum)]
  # transpose
  arr_transposed = []
  for i in range(rowNum):
    for j in range(len(arr)):
      if i < len(arr[j]):
        if i >= len(arr_transposed):
          arr_transposed.append(bytearray())
        arr_transposed[i].append(arr[j][i])
  # join the 2D array into a byte string
  result = b''.join(arr_transposed[i] for i in range(rowNum))
  # remove the padding
  result = result.rstrip(b'x\00')
  return result