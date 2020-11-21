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
# 因为是高IO低计算，所以建议salloc节点上去多并行几个jobs
snakemake --jobs 32 --cores 24 --snakefile Snakefile -p
# 或者也可以这样，就是浪费点儿资源
snakemake --profile slurm --jobs 6 --cores 24 --snakefile Snakefile -p
```

