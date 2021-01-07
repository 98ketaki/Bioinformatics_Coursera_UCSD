def PatternToNumber(Pattern):
    Len = len(Pattern)
    nuc_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    Number= 0
    for i in range(Len):
        Number += nuc_dict[Pattern[i]]*4**(Len-i-1)
    return Number

def ComputingFrequencies(Text, k):
  FrequencyArray = [0] * (4**k)
  for i in range(len(Text)-k+1):
    Pattern = Text[i:(i+k)]
    j = PatternToNumber(Pattern)
    FrequencyArray[j] = FrequencyArray[j] + 1
  return (FrequencyArray)
print(ComputingFrequencies("TCTTGCC", 2))   
        








