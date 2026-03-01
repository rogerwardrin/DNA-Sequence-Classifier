def extract_chr1(input_fasta, output_fasta):
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        writing = False

        for line in infile:
            if line.startswith(">"):
                header = line.lower()
                if header.startswith(">nc_") and "chromosome 1" in header:
                    writing = True
                    print(f"Found primary chromosome 1 header : {line.strip()}")
                elif writing:
                    print("Chromosome 1 extraction complete.")
                    break
            else:
                if writing:
                    outfile.write(line)
        print("Done.")
                
