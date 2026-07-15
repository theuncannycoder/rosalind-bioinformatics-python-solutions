# Problem: 	Counting Point Mutations
# Rosalind ID: HAMM
	s = input().strip()
t = input().strip()
distance = sum(1 for a, b in zip(s, t) if a != b)
print(distance)
