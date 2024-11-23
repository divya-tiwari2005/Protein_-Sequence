from Bio.Blast import NCBIWWW, NCBIXML
from Bio import BiopythonWarning
import warnings

# Ignore warnings from Biopython (optional)
warnings.simplefilter('ignore', BiopythonWarning)

# Your protein sequence
sequence = "FDVDDYMMYDDKLYVGYYRWSLSSEPCQISDMIKILQFMFEIVLNKYGLH"

try:
    print("Starting BLAST search...")
    # Perform the BLAST search using a different database
    result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence, expect=1e-3)
    print("BLAST search completed.")
    
    with open("blast_result.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    print("Results saved to blast_result.xml.")
    
    # Read and parse the results
    with open("blast_result.xml") as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            print(f"Query: {blast_record.query}")
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    print(f"Match: {alignment.title}")
                    print(f"Score: {hsp.score}")
                    if hasattr(hsp, 'evalue'):
                        print(f"E-value: {hsp.evalue}")
                    print(f"Query Start: {hsp.query_start}, Query End: {hsp.query_end}")
                    if hasattr(hsp, 'hit_start') and hasattr(hsp, 'hit_end'):
                        print(f"Match Start: {hsp.hit_start}, Match End: {hsp.hit_end}")
                    print(f"Alignment:\n{hsp.sbjct}")
                    print(f"Identities: {hsp.identities}")
                    print(f"Gaps: {hsp.gaps}")
                    print(f"Alignment Length: {hsp.align_length}")
                    print(f"Percent Identity: {hsp.identities / hsp.align_length * 100:.2f}%")
                    print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")
