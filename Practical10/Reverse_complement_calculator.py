def reverse(DNAs):
    '''
    Input: DNAs, a string formed by ['A','a','T','t','C','c','G','g']
	Returns a string
    '''
    seq = list(DNAs)
    #Uniform case
    for i in range(len(seq)):
        if (seq[i]=='A')or(seq[i]=='a'):
            seq[i]='T'
            continue
        if (seq[i]=='C')or(seq[i]=='c'):
            seq[i]='G'
            continue
        if (seq[i]=='G')or(seq[i]=='g'):
            seq[i]='C'
            continue
        if (seq[i]=='T')or(seq[i]=='t'):
            seq[i]='A'
            continue
    s = ''
    #get reverse complement
    for i in range(len(seq)-1,-1,-1):
        s = s + str(seq[i])
    print("Reverse complement:",s)


DNAseq = input("DNA sequence:")
reverse(DNAseq)