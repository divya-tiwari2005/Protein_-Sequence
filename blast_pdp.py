
from Bio.Blast import NCBIWWW, NCBIXML
import warnings

# Ignore Biopython warnings
warnings.simplefilter('ignore')

# Your protein sequence
sequence = "EVGMCFNRQPQCEIKTVVINDAGPTFRYWDNEHNTEAIMGVCMIHTGDYD"
try:
    # Perform BLAST search against the PDB database
    result_handle = NCBIWWW.qblast("blastp", "pdb", sequence)

    # Save the result in an XML file
    with open("blast_pdb_result.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    # Read and parse the BLAST results
    with open("blast_pdb_result.xml") as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            print(f"Query: {blast_record.query}")
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    print(f"Match: {alignment.title}")
                    print(f"Score: {hsp.score}")
                    print(f"E-value: {hsp.expect}")
                    print(f"Query Start: {hsp.query_start}, Query End: {hsp.query_end}")
                    print(f"Alignment:\n{hsp.query}")
                    print(f"Identities: {hsp.identities}")
                    print(f"Percent Identity: {(hsp.identities / hsp.align_length) * 100:.2f}%")
                    print(f"Gaps: {hsp.gaps}")
                    print(f"Alignment Length: {hsp.align_length}")
                    print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")
