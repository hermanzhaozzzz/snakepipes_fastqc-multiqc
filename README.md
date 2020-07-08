---
Author: Herman Zhao
Email: hermanzhaozzzz@gmail.com
---
Env:
  - conda create py37 python=3.7 -c bioconda
  - conda activate py37
   * conda install -c bioconda fastqc=0.11.8
   * conda install -c bioconda multiqc=1.7
---
Usage:
   1. git clone git@github.com:hermanzhaozzzz/snakepipes_fastqc-multiqc.git
   2. set the conda env -- py37 well
   2. cd snakepipes_fastqc-multiqc
   3. edit Snakefile
       - software
       - SAMPLES
       - put your fastq.gz files in ../reads
       - fix your input names
       - snakemake --profile slurm --jobs 6 # for myself

