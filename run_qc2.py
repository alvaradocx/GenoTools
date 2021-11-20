import pandas as pd
import argparse
import shutil
import os
import subprocess

# local imports
from QC.qc import callrate_prune, het_prune, sex_prune, related_prune, variant_prune, avg_miss_rates
from Ancestry.ancestry2 import run_ancestry, split_cohort_ancestry
from QC.utils import shell_do

parser = argparse.ArgumentParser(description='Arguments for Genotyping QC (data in Plink .bim/.bam/.fam format)')
parser.add_argument('--geno', type=str, default='nope',
                    help='Genotype: (string file path). Path to PLINK format genotype file, everything before the *.bed/bim/fam [default: nope].')
parser.add_argument('--ref', type=str, default='nope',
                    help='Genotype: (string file path). Path to PLINK format reference genotype file, everything before the *.bed/bim/fam.')
parser.add_argument('--ref_labels', type=str, default='nope',
                    help='tab-separated plink-style IDs with ancestry label (FID  IID label) with no header')
parser.add_argument('--out', type=str, default='nope', help='Prefix for output (including path)')

args = parser.parse_args()

geno_path = args.geno
ref_panel = args.ref
ref_labels = args.ref_labels
out_path = args.out

# sample size
fam_df = pd.read_csv(f'{geno_path}.fam', sep='\s+', header=None)
n = fam_df.shape[0]

# sample-level pruning and metrics
missing_path = f'{geno_path}_missing'
avg_miss = avg_miss_rates(geno_path, missing_path)
# avg_miss

callrate_out = f'{geno_path}_callrate'
callrate = callrate_prune(geno_path, callrate_out)

sex_out = f'{callrate_out}_sex'
sex = sex_prune(callrate_out, sex_out)

# run ancestry methods
ancestry_out = f'{sex_out}_ancestry'
ancestry = run_ancestry(geno_path=sex_out, out_path=ancestry_out, ref_panel=ref_panel, ref_labels=ref_labels)

# get ancestry counts to add to output .h5 later
ancestry_counts_df = pd.DataFrame(ancestry['metrics']['predicted_counts']).reset_index()
ancestry_counts_df.columns = ['label', 'count']

# split cohort into individual ancestry groups
pred_labels_path = ancestry['output']['predicted_labels']['labels_outpath']
cohort_split = split_cohort_ancestry(geno_path=sex_out, labels_path=pred_labels_path, out_path=ancestry_out)
