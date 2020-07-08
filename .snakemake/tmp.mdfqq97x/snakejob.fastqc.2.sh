#!/bin/bash
# properties = {"type": "single", "rule": "fastqc", "local": false, "input": ["../fastq/293T-RNASeq-BE4-0706-rep1_R1.fastq.gz", "../fastq/293T-RNASeq-BE4-0706-rep1_R2.fastq.gz", "../fastq/293T-RNASeq-M2-0706-rep1_R1.fastq.gz", "../fastq/293T-RNASeq-M2-0706-rep1_R2.fastq.gz"], "output": ["../qc/fastqc/293T-RNASeq-BE4-0706-rep1_R1_fastqc.html", "../qc/fastqc/293T-RNASeq-BE4-0706-rep1_R2_fastqc.html", "../qc/fastqc/293T-RNASeq-M2-0706-rep1_R1_fastqc.html", "../qc/fastqc/293T-RNASeq-M2-0706-rep1_R2_fastqc.html"], "wildcards": {}, "params": {"threads": "24"}, "log": ["../qc/fastqc.log"], "threads": 1, "resources": {}, "jobid": 2, "cluster": {}}
cd /gpfs/user/zhaohuanan/3.project/6.2020-07_CBE_RNA-seq_off-target/snakepipes_fastqc-multiqc && \
/home/zhaohuanan/anaconda3/envs/snakemake/bin/python \
-m snakemake ../qc/fastqc/293T-RNASeq-M2-0706-rep1_R1_fastqc.html --snakefile /gpfs/user/zhaohuanan/3.project/6.2020-07_CBE_RNA-seq_off-target/snakepipes_fastqc-multiqc/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /gpfs/user/zhaohuanan/3.project/6.2020-07_CBE_RNA-seq_off-target/snakepipes_fastqc-multiqc/.snakemake/tmp.mdfqq97x ../fastq/293T-RNASeq-BE4-0706-rep1_R1.fastq.gz ../fastq/293T-RNASeq-BE4-0706-rep1_R2.fastq.gz ../fastq/293T-RNASeq-M2-0706-rep1_R1.fastq.gz ../fastq/293T-RNASeq-M2-0706-rep1_R2.fastq.gz --latency-wait 60 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://bitbucket.org/snakemake/snakemake-wrappers/raw/ \
  -p --nocolor \
--notemp --no-hooks --nolock --mode 2  --allowed-rules fastqc  && exit 0 || exit 1

