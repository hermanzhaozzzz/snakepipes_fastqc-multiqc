# _*_ coding: UTF-8 _*_
import os
########################################################################
# ZHAO Huanan
# fastqc + multiqc pipeline
######################################################################## 

# --------------------------------------------------------------->>>>>>>
# pipeline
# --------------------------------------------------------------->>>>>>>
# 1. fastqc
# 2. multiqc

# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
    'EMX1-digenome-5-1_combined',
    'EMX1-digenome-5-1_combined',
    'EMX1-digenome-5-2_combined',
    'EMX1-digenome-5-2_combined',
    'cas9-RUX-25_combined',
    'cas9-RUX-25_combined',
    'cpf1-RUX-21_combined',
    'cpf1-RUX-21_combined'
]

THREADS = '24'





# --------------------------------------------------------------->>>>>>>
# software
# --------------------------------------------------------------->>>>>>>
# make sure the fastqqc and the multiqc are in you PATH
# get the application path
with os.popen("which fastqc") as path:
    FASTQC = path.read().strip()
    print('PATH fastqc:', FASTQC)
with os.popen("which multiqc") as path:
    MULTIQC = path.read().strip()
    print('PATH multiqc:', MULTIQC)

# --------------------------------------------------------------->>>>>>>
# start
# --------------------------------------------------------------->>>>>>>
        
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule all
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule all:
    input:
        expand("../fastq/{sample}_R1.fastq.gz", sample=SAMPLES),
        expand("../fastq/{sample}_R2.fastq.gz", sample=SAMPLES),
        expand("../qc/fastqc/{sample}", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"
        
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule fastqc: 
    input: 
        "../fastq/{sample}_R1.fastq.gz",
        "../fastq/{sample}_R2.fastq.gz"
    output: 
        directory("../qc/fastqc/{sample}")
    log:
        "../qc/fastqc/{sample}.log"
    shell:
        """
        mkdir -p {output}
        {FASTQC} -o {output} -t {THREADS} \
        {input[0]} {input[1]} > {log} 2>&1
        """
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule multiqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule multiqc: 
    input: 
        expand("../qc/fastqc/{sample}",sample=SAMPLES)
    output:
        "../qc/multiqc/multiqc_report.html"
    log:
        "../qc/multiqc/multiqc_report.log"
    shell: 
        """
        {MULTIQC} ../qc/fastqc -o ../qc/multiqc --no-data-dir > {log} 2>&1
        """