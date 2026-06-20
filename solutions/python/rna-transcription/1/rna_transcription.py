def to_rna(dna_strand):
    answer = ""
    for letter in dna_strand:
        if letter == "G":
            answer += "C"
        if letter == "C":
            answer += "G"
        if letter == "T":
            answer += "A"
        if letter == "A":
            answer += "U"
    return answer
    
            
