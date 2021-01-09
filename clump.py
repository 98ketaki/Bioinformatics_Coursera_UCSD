def NumberToSymbol(index):
  letters = ["A", "C", "G", "T"]
  return (letters[index])

def SymbolToNumber(symbol):
  letters = ["A", "C", "G", "T"]
  return (letters.index(symbol))

def PatternToNumber(Pattern):
  if Pattern == "" : 
    return (0)
  symbol = Pattern[-1]
  Prefix = Pattern[:-1]
  return (4*PatternToNumber(Prefix) + SymbolToNumber(symbol))

def NumberToPattern(index, k):
  if k == 1:
    return NumberToSymbol(index)
  prefixIndex = index // 4
  r = index % 4
  symbol = NumberToSymbol(r)
  PrefixPattern = NumberToPattern(prefixIndex, k-1)
  return (str(PrefixPattern) + str(symbol))

def ComputingFrequencies(Text, k):
  FrequencyArray = [0] * (4**k)
  for i in range(len(Text)-k+1):
    Pattern = Text[i:(i+k)]
    j = PatternToNumber(Pattern)
    FrequencyArray[j] = FrequencyArray[j] + 1
  return (FrequencyArray)

def ClumpFindingPro(Genome, k, L, t):
  FrequentPatterns = set() 
  Clump = [0] * (4**k) 
  Text = Genome[:L]
  FrequencyArray = ComputingFrequencies(Text, k)

  for index in range(4**k):
      if FrequencyArray[index] >= t:
        Clump[index] = 1 
  for i in range(1, len(Genome) -L):
    FirstPattern = Genome [(i-1): (i+k-1)]
    index1 = PatternToNumber(FirstPattern)
    FrequencyArray[index1] -= 1
    LastPattern = Genome[(i+L-k): (i+L)]
    index2 = PatternToNumber(LastPattern)
    FrequencyArray[index2] += 1
    if FrequencyArray[index2] >= t:
      Clump[index2] = 1
  for i in range(4**k):
    if Clump[i] == 1:
      Pattern = NumberToPattern(i, k) 
      FrequentPatterns.add(Pattern)
  return FrequentPatterns


print (ClumpFindingPro("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4))