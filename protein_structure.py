import random
from Bio.PDB import PDBParser, PDBIO

# Step 1: Generate Random Protein Sequence
def generate_random_sequence(length):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"  # Standard amino acids
    return ''.join(random.choice(amino_acids) for _ in range(length))

protein_sequence = generate_random_sequence(50)  # Generate a random protein of length 50
print("Generated Protein Sequence:", protein_sequence)

# Step 2: Save Sequence to a File
with open("protein_sequence.fasta", "w") as f:
    f.write(f">Random_Protein\n{protein_sequence}\n")
print("Protein sequence saved to protein_sequence.fasta.")

# Step 3: (Mock Structure Prediction)
# Normally, here you'd call Modeller or AlphaFold to predict the structure.
# For demonstration, we will simulate this by creating a mock PDB file.

mock_pdb_content = """
ATOM      1  N   MET A   1      20.154  34.234  27.568  1.00 20.00           N  
ATOM      2  CA  MET A   1      21.217  35.123  27.251  1.00 20.00           C  
ATOM      3  C   MET A   1      22.643  34.789  27.899  1.00 20.00           C  
ATOM      4  O   MET A   1      23.428  35.688  28.474  1.00 20.00           O  
ATOM      5  CB  MET A   1      21.012  36.421  26.633  1.00 20.00           C  
"""

# Save the mock PDB content to a file
with open("mock_protein_model.pdb", "w") as f:
    f.write(mock_pdb_content)
print("Mock PDB model saved to mock_protein_model.pdb.")

# Step 4: Analyze the Structure
parser = PDBParser()
structure = parser.get_structure('Mock_Protein', 'mock_protein_model.pdb')

# Analyze the structure
for model in structure:
    for chain in model:
        print(f"Chain {chain.id} has {len(chain)} residues.")
        for residue in chain:
            print(f"Residue: {residue.resname} at {residue.id}")

print("Structure analysis complete.")
