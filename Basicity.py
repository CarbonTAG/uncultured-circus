## FASTA Sequence Basicity Calculator (FSBC)
# basic amino acids are (R)arginine, (K)lysine and (H)histadine and acidic amino aacids (D)Aspartate  (E)Glutamate
# basic residue R, K, H
# acidic residues
# aromatic residues 

Seq_name = input('Name your sequence: ')
Seq = input('Enter your FASTA sequence: ')

M = ['R', 'K', 'H', ]

N = ['D', 'E', ]

Total = 0
Total1 = 0

for s in Seq:
    if s.__contains__(M[0]) or s.__contains__(M[1]) or s.__contains__(M[2]):
        Total += 1
    else:
        pass

for s in Seq:
    if s.__contains__(N[0]) or s.__contains__(N[1]):
        Total1 += 1
    else:
        pass

print(Seq_name, ':')
print('Sequence:', Seq)
print('Sequence length: ',len(Seq))

if 20 <= len(Seq) <= 50:
    print('The sequence', Seq_name, 'is ok.')


elif len(Seq) > 50:\
    print('The sequence', Seq_name,' is too large for antiviral activity')
else:
     print('The sequence', Seq_name, 'is too short to give antiviral activity')

print('There are', Total, 'basic amino acids.')
print('There are', Total1, 'acidic amino acids.')
print('Percentage basicity of', Seq_name, 'is: ', (Total / (Total1 + Total) * 100), '%')
