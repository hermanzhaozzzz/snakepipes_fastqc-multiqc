---
Author: Herman Zhao
Email: hermanzhaozzzz@gmail.com
---
Env:
   * conda install -c bioconda fastqc=0.11.8
   * conda install -c bioconda multiqc=1.7
---
Usage:
   1. git@github.com:hermanzhaozzzz/snakepipes_fastqc-multiqc.git
   2. cd snakepipes_fastqc-multiqc
   3. edit Snakefile
       - software
       - SAMPLES
       - put your fastq.gz files in ../reads
       - fix your input names
       - snakemake --profile slurm --jobs 6 # for myself

