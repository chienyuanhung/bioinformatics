# put your python code here
import random
# score function to evaluate motif 
def Score(Motif):
    a = len(Motif)
    b = len(Motif[0])
    count = 0
    for i in range(b):
        countA = 0
        countC = 0
        countG = 0
        countT = 0
        for j in range(a):
            if Motif[j][i] == 'A':
                countA += 1
            elif Motif[j][i] == 'C':
                countC += 1
            elif Motif[j][i] == 'G':
                countG += 1
            elif Motif[j][i] == 'T':
                countT += 1
        count = count+ countA + countC + countG + countT - max(countA, countC, countG, countT)
    return count

# profile functions: get the probability profile for motifs
def profile(motif):
    a = len(motif)
    b = len(motif[0])
    prob = {'A': [0]*b, 'C': [0]*b, 'G': [0]*b, 'T': [0]*b} 
    for i in range(b):
        countA = 0
        countC = 0
        countG = 0
        countT = 0
        for m in range(a):
            if motif[m][i] == 'A':
                countA += 1
            elif motif[m][i] == 'C':
                countC += 1
            elif motif[m][i] == 'G':
                countG += 1
            elif motif[m][i] == 'T':
                countT += 1
        sum_count = countA + countC+ countG+ countT
        prob['A'][i] = countA/sum_count
        prob['C'][i] = countC/sum_count
        prob['G'][i] = countG/sum_count
        prob['T'][i] = countT/sum_count
    return prob

# modified profile functions with Laplace rule: get the probability profile for motifs, add pseodocount
def modified_profile(motif, pseudocount):
    a = len(motif)
    b = len(motif[0])
    prob = {'A': [0]*b, 'C': [0]*b, 'G': [0]*b, 'T': [0]*b} 
    for i in range(b):
        countA = pseudocount
        countC = pseudocount
        countG = pseudocount
        countT = pseudocount
        for j in range(a):
            if motif[j][i] == 'A':
                countA += 1
            elif motif[j][i] == 'C':
                countC += 1
            elif motif[j][i] == 'G':
                countG += 1
            elif motif[j][i] == 'T':
                countT += 1
        sum_count = countA + countC+ countG+ countT
        prob['A'][i] = countA/sum_count
        prob['C'][i] = countC/sum_count
        prob['G'][i] = countG/sum_count
        prob['T'][i] = countT/sum_count
    return prob

# funcitions return the most probable kmer according to the profile
def ProfileMostProbableKmer(text, k, profile):
    final = 0
    a = len(text)
    final_text = text[:k]
    for i in range(a-k+1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            if pattern[j] == 'A':
                prob = prob * profile['A'][j]
            elif pattern[j] == 'C':
                prob = prob * profile['C'][j]
            elif pattern[j] == 'G':
                prob = prob * profile['G'][j]
            elif pattern[j] == 'T':
                prob = prob * profile['T'][j]
        if prob > final:
            final = prob
            final_text= text[i: i+k]
    return final_text 

# randomlty generate motif from each DNA sequence
def gen_motif(Dna, k):
    a = len(Dna[1])
    motifs = []
    for i in Dna:
        b = random.randint(0, a-k)
        motif = i[b: b+k]
        motifs.append(motif)
    return motifs

def motifs_from_profile(dna, k, profile):
    motifs = []
    for i in dna:
        motif = ProfileMostProbableKmer(i, k, profile)
        motifs.append(motif)
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    motifs = gen_motif(Dna, k)
    best_motifs = gen_motif(Dna, k)
    while True:
        new_profile = modified_profile(motifs,1)
        motifs = motifs_from_profile(Dna, k, new_profile)
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs
        
    

import sys        
lines = sys.stdin.read().splitlines()       

k, t = map(int, lines[0].split(" "))
Dna = []
for i in range(1, len(lines)):
    Dna.append(lines[i])

M = RandomizedMotifSearch(Dna, k, t)
bMotifs = M
N = 25
for i in range(N+1):
    M = RandomizedMotifSearch(Dna, k, t)
    if Score(M) < Score(bMotifs):
         bMotifs = M
    else:
        bestMotifs = bMotifs    
        
print ('\n'.join(bestMotifs))