# Problem: Computing GC Content
# Rosalind ID: GC

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100
data = []
current_id = ""
current_seq = ""
try:
    while True:
        line = input().strip()
        if line.startswith(">"):
            if current_id:
                data.append((current_id, current_seq))
            current_id = line[1:]
            current_seq = ""
        else:
            current_seq += line
except EOFError:
    if current_id:
        data.append((current_id, current_seq))
max_id = ""
max_gc = 0
for id_, seq in data:
    gc = gc_content(seq)
    if gc > max_gc:
        max_gc = gc
        max_id = id_

print(max_id)
print(f"{max_gc:.6f}")
