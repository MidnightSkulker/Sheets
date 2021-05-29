
def sumOfSquaresDifference(n: int) -> int:
    squareOfSum = int((n * n * (n + 1) * (n + 1)) / 4)
    sumOfSquares = int((n * (n + 1) * (2 * n + 1)) / 6)
    return squareOfSum - sumOfSquares
