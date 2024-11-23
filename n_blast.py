from Bio.Blast import NCBIWWW, NCBIXML

# Step 1: Define your protein sequence
protein_sequence = """from Bio.Blast import NCBIWWW, NCBIXML"""

# Step 1: Define your protein sequence
protein_sequence = "FDVDDYMMYDDKLYVGYYRWSLSSEPCQISDMIKILQFMFEIVLNKYGLH"


# Step 2: Run the sequence against the NCBI BLAST web service
print("Running BLAST search...")
result_handle = NCBIWWW.qblast("blastp", "nr", protein_sequence)

# Step 3: Save the BLAST results to an XML file
with open("blast_results.xml", "w") as out_file:
    out_file.write(result_handle.read())

# Step 4: Parse the BLAST results
result_handle = open("blast_results.xml")
blast_record = NCBIXML.read(result_handle)

# Step 5: Print the top 5 BLAST hits
for alignment in blast_record.alignments[:5]:
    print(f"****Alignment****")
    print(f"Sequence: {alignment.title}")
    print(f"Length: {alignment.length}")
    for hsp in alignment.hsps:
        print(f"E-value: {hsp.expect}")
        print(f"Identities: {hsp.identities}")
        print(f"Alignment: \n{hsp.query}\n{hsp.match}\n{hsp.sbjct}")
