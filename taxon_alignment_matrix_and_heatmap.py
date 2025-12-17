import glob
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. Read FASTA alignments
# --------------------------------------------------

fasta_files = sorted(glob.glob("*.fasta"))

alignment_taxa = {}
all_taxa = set()

for fasta in fasta_files:
    taxa_in_alignment = set()
    for record in SeqIO.parse(fasta, "fasta"):
        taxon = record.id  # adjust here if headers need parsing
        taxa_in_alignment.add(taxon)
        all_taxa.add(taxon)
    alignment_taxa[fasta] = taxa_in_alignment

all_taxa = sorted(all_taxa)

# --------------------------------------------------
# 2. Build presence/absence matrix
# --------------------------------------------------

matrix = []

for taxon in all_taxa:
    row = {"taxon": taxon}
    for fasta in fasta_files:
        row[fasta] = 1 if taxon in alignment_taxa[fasta] else 0
    matrix.append(row)

df = pd.DataFrame(matrix)

# Add total number of alignments per taxon
df["total_alignments"] = df.drop(columns=["taxon"]).sum(axis=1)

# Save table
df.to_csv("taxon_alignment_presence_absence.csv", index=False)

# --------------------------------------------------
# 3. Prepare data for heatmap
# --------------------------------------------------

df_sorted = df.sort_values("total_alignments", ascending=False)

taxa = df_sorted["taxon"]
data = df_sorted.drop(columns=["taxon", "total_alignments"])

# --------------------------------------------------
# 4. Plot colored heatmap (0/1)
# --------------------------------------------------

cmap = sns.color_palette(["#f2f2f2", "#2166ac"])  # absence / presence

plt.figure(figsize=(16, 22))

sns.heatmap(
    data,
    cmap=cmap,
    linewidths=0.3,
    linecolor="white",
    cbar=True,
    xticklabels=False,
    yticklabels=taxa
)

plt.xlabel("Alignments")
plt.ylabel("Taxa")
plt.title("Presence (1) and Absence (0) of Taxa Across Alignments")

# Customize colorbar
cbar = plt.gca().collections[0].colorbar
cbar.set_ticks([0.25, 0.75])
cbar.set_ticklabels(["Absent (0)", "Present (1)"])

plt.tight_layout()
plt.savefig("heatmap_taxon_alignment_colored.png", dpi=300)
plt.savefig("heatmap_taxon_alignment_colored.pdf")
plt.close()
