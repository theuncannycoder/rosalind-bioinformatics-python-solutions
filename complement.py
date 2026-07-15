# Problem: Complementing a Strand of DNA
#Rosalind ID: REVC
s = input().strip()
table = str.maketrans('ATCG', 'TAGC')
reverse_complement = s.translate(table)[::-1]
print(reverse_complement)
