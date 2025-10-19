def to_rna(dna_strand):
    """Transcribe a DNA strand to its RNA complement.
    
    Transcription rules:
    G -> C
    C -> G
    T -> A
    A -> U
    
    :param dna_strand: str - DNA sequence.
    :return: str - RNA complement sequence.
    
    Examples:
    >>> to_rna("C")
    'G'
    >>> to_rna("G")
    'C'
    >>> to_rna("T")
    'A'
    >>> to_rna("A")
    'U'
    >>> to_rna("ACGTGGTCTTAA")
    'UGCACCAGAAUU'
    """
    # DNA to RNA transcription mapping
    transcription_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    
    # Transcribe each nucleotide
    return ''.join(transcription_map[nucleotide] for nucleotide in dna_strand)


# Alternative approaches:

def to_rna_v2(dna_strand):
    """Alternative using str.translate()."""
    translation_table = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(translation_table)


def to_rna_v3(dna_strand):
    """Alternative using replace() chain."""
    return (dna_strand
            .replace('G', 'c')
            .replace('C', 'g')
            .replace('T', 'a')
            .replace('A', 'u')
            .upper())


def to_rna_v4(dna_strand):
    """Alternative with explicit mapping."""
    result = []
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            result.append('C')
        elif nucleotide == 'C':
            result.append('G')
        elif nucleotide == 'T':
            result.append('A')
        elif nucleotide == 'A':
            result.append('U')
    return ''.join(result)