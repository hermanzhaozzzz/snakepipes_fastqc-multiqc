# _*_ coding: UTF-8 _*_

########################################################################
# ZHAO Huanan
# 2020-05-04
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

# conda install -c bioconda fastqc=0.11.8
FASTQC = "/home/zhaohuanan/zhaohn_HD/miniconda3/bin/fastqc"

# conda install -c bioconda multiqc=1.7
MULTIQC = "/home/zhaohuanan/zhaohn_HD/miniconda3/bin/multiqc"





# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
"DigenomeSeq_EMX1",
"DigenomeSeq_HEK4"
]
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule all
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule all:
    # 有点特殊，输出和输入文件名只能有R1.fastq.gz和_fastqc.html的区别，前面不能有区别！要改就得全改！
    input:
        expand("../fastq/{sample}_R1.fastq.gz",sample=SAMPLES),
        expand("../fastq/{sample}_R2.fastq.gz",sample=SAMPLES),
        expand("../qc/fastqc/{sample}_R1_fastqc.html", sample=SAMPLES),
        expand("../qc/fastqc/{sample}_R2_fastqc.html", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule fastqc: 
    input: 
        "../fastq/{sample}_R1.fastq.gz",
        "../fastq/{sample}_R2.fastq.gz"
    output: 
        "../qc/fastqc/{sample}_R1_fastqc.html",
        "../qc/fastqc/{sample}_R2_fastqc.html"
                # the suffix _fastqc.zip is necessary the same with SAMPLES raw name suffix, for multiqc to find the file. 
                # If not using multiqc, you are free to choose an arbitrary filename
    params: 
        threads = "24"
    log:
        "../qc/fastqc_{sample}.log"
    shell:
        """
        {FASTQC} -o ../qc/fastqc -t {params.threads} \
        {input[0]} {input[1]} 2>{log}
        """
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule multiqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule multiqc: 
    input: 
        expand(["../qc/fastqc/{sample}_R1_fastqc.html",
                "../qc/fastqc/{sample}_R2_fastqc.html"], sample=SAMPLES)
                # the suffix XXX_fastqc.zip is necessary the same with SAMPLES raw name suffix, for multiqc to find the file. 
    output:
        "../qc/multiqc/multiqc_report.html"
    log:
        "../qc/multiqc.log"
    shell: 
        """
        {MULTIQC} ../qc -o ../qc/multiqc --no-data-dir 2>{log}
        """