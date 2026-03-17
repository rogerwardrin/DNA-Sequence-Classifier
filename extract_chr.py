import re

def extract_chr1(input_fasta, output_fasta, chr):
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        writing = False

        for line in infile:
            if line.startswith(">"):
                header = line.lower()
                if header.startswith(">nc_"):
                    matched = False
                    for i in chr:
                        if re.search(rf"chromosome {i}\b",header):
                            if writing:
                                print(f"Chromosome {current_chr} extraction complete.")
                            writing = True
                            current_chr = i
                            print(f"Found primary chromosome {i} header : {line.strip()}")
                            matched = True
                            break

                        if not matched and writing:
                            print(f"Chromosome {current_chr} extraction complete.")
                            writing = False
            elif writing:
                    outfile.write(line)
        print("Done.")
                
