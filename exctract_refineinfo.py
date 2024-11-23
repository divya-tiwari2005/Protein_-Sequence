from Bio.Blast import NCBIXML

# Open the refined BLAST XML result file
with open("blast_result.xml") as result_file:
    blast_record = NCBIXML.read(result_file)

# Go through each alignment to print key information
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print(f"Query: {blast_record.query}")
        print(f"Match: {alignment.title}")
        print(f"Accession: {alignment.accession}")
        print(f"Score: {hsp.score}")
        print(f"E-value: {hsp.expect}")
        print(f"Query Start: {hsp.query_start}, Query End: {hsp.query_end}")
        print(f"Match Start: {hsp.sbjct_start}, Match End: {hsp.sbjct_end}")
        print(f"Alignment: {hsp.query}")
        print(f"Identities: {hsp.identities}")
        print(f"Gaps: {hsp.gaps}")
        print(f"Alignment Length: {hsp.align_length}")
        print(f"Percent Identity: {100 * hsp.identities / hsp.align_length:.2f}%")
        print("--------------------------------------------------")
