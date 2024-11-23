from Bio import ExPASy, SwissProt

def get_protein_info(uniprot_id):
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)
    return record

# Example UniProt ID for a known protein
uniprot_id = "P69905"  # Hemoglobin subunit alpha
protein_info = get_protein_info(uniprot_id)
print(f"Description: {protein_info.description}")
print(f"Organism: {protein_info.organism}")
print(f"Sequence Length: {len(protein_info.sequence)}")
