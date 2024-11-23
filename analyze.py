from Bio.SeqUtils.ProtParam import ProteinAnalysis

protein_sequence = "EVGMCFNRQPQCEIKTVVINDAGPTFRYWDNEHNTEAIMGVCMIHTGDYD"
analyzed_seq = ProteinAnalysis(protein_sequence)

molecular_weight = analyzed_seq.molecular_weight()
instability_index = analyzed_seq.instability_index()
gravy = analyzed_seq.gravy()

print(f"Molecular Weight: {molecular_weight}")
print(f"Instability Index: {instability_index} (Stability below 40 is stable)")
print(f"GRAVY (Hydrophobicity): {gravy}")
