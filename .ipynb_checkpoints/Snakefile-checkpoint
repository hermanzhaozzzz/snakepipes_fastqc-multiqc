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
FASTQC = "/home/zhaohuanan/zhaohn_HD/1.apps/anaconda3/envs/py37/bin/fastqc"
# conda install -c bioconda multiqc=1.7
MULTIQC = "/home/zhaohuanan/zhaohn_HD/1.apps/anaconda3/envs/py37/bin/multiqc"
# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
    "test",
    "test2"
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
        expand(["../reads/{sample}_combined_R1.fastq.gz",
                 "../reads/{sample}_combined_R2.fastq.gz"], sample=SAMPLES)
    output: 
        expand(["../qc/fastqc/{sample}_combined_R1_fastqc.html",
                "../qc/fastqc/{sample}_combined_R2_fastqc.html"], sample=SAMPLES)
    params: 
        threads = "24"
    shell:
        """
        {FASTQC} -o ../qc/fastqc -t {params.threads} \
        {input}
        """
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule multiqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule multiqc: 
    input: 
        expand(["../qc/fastqc/{sample}_combined_R1_fastqc.html",
                "../qc/fastqc/{sample}_combined_R2_fastqc.html"], sample=SAMPLES)
    output:
        "../qc/multiqc/multiqc_report.html"
    shell: 
        """
        {MULTIQC} ../qc -o ../qc/multiqc --no-data-dir
        """
        