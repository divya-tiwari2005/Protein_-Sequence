from Bio.Blast import NCBIWWW, NCBIXML
from Bio import BiopythonWarning
import warnings

# Ignore warnings from Biopython (optional)
warnings.simplefilter('ignore', BiopythonWarning)

sequence = "EVGMCFNRQPQCEIKTVVINDAGPTFRYWDNEHNTEAIMGVCMIHTGDYD"

try:
    result_handle = NCBIWWW.qblast("blastp", "nr", sequence)
    with open("blast_result.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    # Read and parse the results
    with open("blast_result.xml") as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            print(f"Query: {blast_record.query}")
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    print(f"Match: {alignment.title}")
                    print(f"Score: {hsp.score}")
                    print(f"E-value: {hsp.evalue}")

except Exception as e:
    print(f"An error occurred: {e}")
