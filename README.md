# Presence–Absence Matrix and Heatmap for Phylogenomic Alignments

This repository provides a **simple, universal pipeline** to summarize and visualize the distribution of taxa across multiple sequence alignments (FASTA files), commonly used in phylogenomics (e.g. UCE, AHE, exons, genes), but applicable to **any multi-FASTA dataset**.

The pipeline produces:
1. A **presence/absence table** (taxa × alignments)
2. A **colored heatmap** (0/1) to visually assess matrix completeness

---

## Overview

Given a directory containing multiple FASTA alignments:

- **Rows** represent taxa (species, samples)
- **Columns** represent alignments (loci)
- **Cells** indicate:
  - `1` → taxon present in that alignment
  - `0` → taxon absent

This approach is useful to:
- Evaluate **matrix completeness**
- Identify **poorly sampled taxa**
- Detect **blocks of loci specific to subsets of taxa**
- Justify filtering thresholds (e.g. 50%, 70% occupancy)
- Provide **supplementary figures** for phylogenomic studies

---

## Requirements

- Python ≥ 3.8
- Required libraries:
  ```bash
  pip install biopython pandas matplotlib seaborn

## Usage 

- Input

A folder containing multiple FASTA files

Each FASTA file represents one alignment (locus)

FASTA headers must contain a taxon identifier (e.g. species name)

Example:

locus_001.fasta
locus_002.fasta
locus_003.fasta
...

- Output

The script generates:

Presence/absence table

taxon_alignment_presence_absence.csv

Colored heatmap

heatmap_taxon_alignment_colored.png

heatmap_taxon_alignment_colored.pdf
