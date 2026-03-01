import pandas as pd
import re

def get_fragments_df(extracted_chr, species,fragment_length):
    print(f"{species}:")
    seq = load_chromosome_as_string(extracted_chr)
    seq = seq.upper()
    seq = re.sub(r'[^ATGC]', 'N', seq)

    fragments = create_fragments(seq,fragment_length)
    return fragments_to_dataframe(fragments, species)

def load_chromosome_as_string(fasta_file):
    sequence_parts = []

    with open(fasta_file,"r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence_parts.append(line.strip())

    sequence = "".join(sequence_parts)
    print("Total length: ", len(sequence))
    return sequence

def create_fragments(sequence, fragment_length):
    fragments = []
    for i in range(0,len(sequence) - fragment_length + 1, fragment_length):
        fragment = sequence[i:i+fragment_length]
        fragments.append(fragment)
    
    print(f"Total Fragments: {len(fragments)}")
    return fragments

def fragments_to_dataframe(fragments, species_label):
    df = pd.DataFrame({"sequence": fragments, "species": species_label})
    return df