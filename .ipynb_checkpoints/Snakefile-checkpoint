# _*_ coding: UTF-8 _*_

########################################################################
# ZHAO Huanan
# 2020-05-04
# fastqc + multiqc pipeline
######################################################################## 
# run on abyss
# /gpfs/user/zhaohuanan/3.project/3.2020-05_BE3andBE4_RNA-seq

# --------------------------------------------------------------->>>>>>>
# pipeline
# --------------------------------------------------------------->>>>>>>
# 1. fastqc
# 2. multiqc
# --------------------------------------------------------------->>>>>>>
# software
# --------------------------------------------------------------->>>>>>>

# conda install -c bioconda fastqc=0.11.8
FASTQC = "/home/zhaohuanan/anaconda3/envs/py37/bin/fastqc"

# conda install -c bioconda multiqc=1.7
MULTIQC = "/home/zhaohuanan/anaconda3/envs/py37/bin/multiqc"





# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
    "BE4-0706-rep1",
    "M2-0706-rep1"
]
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule all
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule all:
    input:
        "../qc/multiqc/multiqc_report.html"
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>


rule fastqc: 
    input: 
        expand(["../fastq/293T-RNASeq-{sample}_R1.fastq.gz",
                 "../fastq/293T-RNASeq-{sample}_R2.fastq.gz"], sample=SAMPLES)
    output: 
        expand(["../qc/fastqc/293T-RNASeq-{sample}_R1_fastqc.html",
                "../qc/fastqc/293T-RNASeq-{sample}_R2_fastqc.html"], sample=SAMPLES)
                # the suffix _fastqc.zip is necessary the same with SAMPLES raw name suffix, for multiqc to find the file. 
                # If not using multiqc, you are free to choose an arbitrary filename
    params: 
        threads = "24"
    log:
        "../qc/fastqc.log"
    shell:
        """
        {FASTQC} -o ../qc/fastqc -t {params.threads} \
        {input} 2>{log}
        """
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule multiqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule multiqc: 
    input: 
        expand(["../qc/fastqc/293T-RNASeq-{sample}_R1_fastqc.html",
                "../qc/fastqc/293T-RNASeq-{sample}_R2_fastqc.html"], sample=SAMPLES)
                # the suffix XXX_fastqc.zip is necessary the same with SAMPLES raw name suffix, for multiqc to find the file. 
    output:
        "../qc/multiqc/multiqc_report.html"
    log:
        "../qc/multiqc.log"
    shell: 
        """
        {MULTIQC} ../qc -o ../qc/multiqc --no-data-dir 2>{log}
        """
        