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
SAMPLES = ['Liu-Untreated-rep1_combined',
 'Liu-Untreated-rep2_combined',
 'Liu-Untreated-rep3_combined',
 'OurATACSeq_1_combined',
 'OurATACSeq_2_combined',
 'OurATACSeq_4_combined',
 'OurATACSeq_5_combined']


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