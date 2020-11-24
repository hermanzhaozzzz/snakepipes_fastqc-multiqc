---
Author: Herman Zhao
Email: hermanzhaozzzz@gmail.com
---


# snakepipes_fastqc-multiqc
## Introduction:
This snakemake pipeline aims to do fastqc and multiqc for many fastq.gz files in a same folder
## Env:
```
conda install snakemake
conda create -n snakepipes_fastqc-multiqc fastqc multiqc 
```
---
## Usage:
1. prepare the file and env.
```
git clone git@github.com:hermanzhaozzzz/snakepipes_fastqc-multiqc.git
conda create -n snakepipes_fastqc-multiqc fastqc multiqc
```
2. fill the "SAMPLE" list in the Snakefile
3. Ensure that dependent programs are installed and added into the PATH variable
3. run
```
cd snakepipes_fastqc-multiqc

# test
snakemake -pr -j 24 -s Snakefile -n
# run
snakemake -pr -j 24 -s Snakefile
```



## Update logs:
- 2020-11-24: 
    - update to a normal format and add log files
    - auto set PATH for fastqc and multiqc(use os.popen(which app).read() to return a path for apps)
    
