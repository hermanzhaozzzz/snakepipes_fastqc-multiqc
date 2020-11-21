# _*_ coding: UTF-8 _*_

########################################################################
# ZHAO Huanan
# 2020-11-17
# fastqc + multiqc pipeline
######################################################################## 
# run on abyss
# --------------------------------------------------------------->>>>>>>
# pipeline
# --------------------------------------------------------------->>>>>>>
# 1. fastqc
# 2. multiqc
# --------------------------------------------------------------->>>>>>>
# software
# --------------------------------------------------------------->>>>>>>
FASTQC = "/home/zhaohuanan/zhaohn_HD/miniconda3/bin/fastqc"
MULTIQC = "/home/zhaohuanan/zhaohn_HD/miniconda3/bin/multiqc"
# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
"TargetSeq-CBE-EMX1-rep1",
"TargetSeq-CBE-EMX2-rep2"
]
# multiprocess
THREADS = '24'
# --------------------------------------------------------------->>>>>>>







# --------------------------------------------------------------->>>>>>>
# start
# --------------------------------------------------------------->>>>>>>


# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule all [# 有点特殊，输出和输入文件名只能有R1.fastq.gz和_fastqc.html的区别，前面不能有区别！要改就得全改！]
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule all:
    input:
        # you should change the file name that you want to put in 
        expand("../fastq/{sample}_R1.fastq.gz",sample=SAMPLES),
        expand("../fastq/{sample}_R2.fastq.gz",sample=SAMPLES),
        # look above
        expand("../qc/fastqc/{sample}_R1_fastqc.html", sample=SAMPLES),
        expand("../qc/fastqc/{sample}_R2_fastqc.html", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule fastqc
#           The suffix _fastqc.zip is necessary the same with SAMPLES raw name suffix, 
#.          for multiqc to find the file. 
#           If not using multiqc, you are free to choose an arbitrary filename
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule fastqc: 
    input: 
        "../fastq/{sample}_R1.fastq.gz",
        "../fastq/{sample}_R2.fastq.gz"
    output: 
        "../qc/fastqc/{sample}_R1_fastqc.html",
        "../qc/fastqc/{sample}_R2_fastqc.html"
    log:
        "../qc/fastqc_{sample}.log"
    shell:
        """
        {FASTQC} -o ../qc/fastqc -t {THREADS} \
        {input[0]} {input[1]} 2>{log}
        """
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule multiqc
#           The suffix XXX_fastqc.zip is necessary the same with SAMPLES raw name suffix, 
#           for multiqc to find the file. 
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule multiqc: 
    input: 
        expand(["../qc/fastqc/{sample}_R1_fastqc.html",
                "../qc/fastqc/{sample}_R2_fastqc.html"], sample=SAMPLES)
    output:
        "../qc/multiqc/multiqc_report.html"
    log:
        "../qc/multiqc.log"
    shell: 
        """
        {MULTIQC} ../qc -o ../qc/multiqc --no-data-dir 2>{log}
        """