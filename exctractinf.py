from Bio.Blast import NCBIWWW, NCBIXML

# Your protein sequence
sequence = "FDVDDYMMYDDKLYVGYYRWSLSSEPCQISDMIKILQFMFEIVLNKYGLH"

print("Starting BLAST search...")

try:
    # Perform BLAST search with refined parameters
    result_handle = NCBIWWW.qblast("blastp", "nr", sequence, expect=1.0, hitlist_size=100)

    # Save the BLAST result to XML
    with open("blast_result.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    print("BLAST search completed. Results saved to blast_result.xml.")

    # Parse the XML results
    with open("blast_result.xml") as result_handle:
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
                    print(f"Gaps: {hsp.gaps}")
                    print(f"Percent Identity: {round((hsp.identities / hsp.align_length) * 100, 2)}%")
                    print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")
