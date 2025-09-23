def to_rna(dna_strand):
    translator = str.maketrans("ACGT", "UGCA")
    return dna_strand.translate(translator)