#!/usr/local/bin/python3
dna=input('the sequence of interest:')
kmersize=eval(input('the kmer length for analysis:'))
mini_freq=eval(input('the threshold frequency of kmers found:'))
def kmer_count():
    kmer_list=[];return_list=[]
    for i in range(0,len(dna)-kmersize+1):
        kmer=dna[i:i+kmersize]
        kmer_list.append(kmer)
    for uni_kmer in set(kmer_list):
        if dna.count(uni_kmer) > mini_freq:
            return_list.append(uni_kmer)
    print(return_list)
kmer_count()
