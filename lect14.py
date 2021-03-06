#!/usr/local/bin/python3
def aas_count(protein,residue):
    residue=residue.upper()
    percent=100*protein.upper().count(residue)/len(protein)
    return percent

#2
def aalist_count(protein,residue_list=['A','I','L','M','F','W','Y','V']):
    percent=0
    for residue in set(residue_list):
        residue=residue.upper()
        percent+=100*protein.upper().count(residue)/len(protein)
    return percent

#3
def base_count(dna,threshold):
    normal_counts=0
    for base in ['A','T','G','C']:     
        normal_counts+=dna.upper().count(base)
    undeter_count_freq=(len(dna)-normal_counts)/len(dna)
    if undeter_count_freq > threshold:
        return True
    else:
        return False

#4
def kmer_count(dna,kmersize,mini_freq):
    if ksize > len(dna) :
        return "Sorry, your kmer length is longer than your DNA (" + str(len(dna)) +" bases)." 
    if ksize < 2 or ksize > 50 :
        return "Sorry, inappropriate kmer length, only 2 to 50 accepted here."
    kmer_list=[]
    for i in range(0,len(dna)-kmersize+1):
        kmer=dna[i:i+kmersize]
        kmer_list.append(kmer)
    for uni_kmer in set(kmer_list):
        if dna.count(uni_kmer) > mini_freq:
            print(uni_kmer.upper(),str(dna.count(uni_kmer)))

