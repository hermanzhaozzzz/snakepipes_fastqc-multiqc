---
Author: Herman Zhao
Email: hermanzhaozzzz@gmail.com
---
Env:
```
conda create -n snakepipes_fastqc-multiqc python=3.7 fastqc=0.11.8 multiqc=1.7 
```
---
Usage:
1. prepare the file and env.
```
git clone git@github.com:hermanzhaozzzz/snakepipes_fastqc-multiqc.git
conda create -n snakepipes_fastqc-multiqc python=3.7 fastqc=0.11.8 multiqc=1.7 
```
2. cd snakepipes_fastqc-multiqc
3. 
```
snakemake --profile slurm --jobs 6 --cores 24 --snakefile Snakefile -p
```

