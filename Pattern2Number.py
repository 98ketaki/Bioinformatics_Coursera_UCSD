def PatternToNumber(Pattern):
    Len = len(Pattern)
    nuc_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    Number= 0
    for i in range(Len):
        Number += nuc_dict[Pattern[i]]*4**(Len-i-1)
    return Number
print(PatternToNumber("ACGCGGCTCTGAAA"))