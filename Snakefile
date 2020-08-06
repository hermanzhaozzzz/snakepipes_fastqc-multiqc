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
FASTQC = "~/miniconda3/envs/snakepipes_fastqc-multiqc/bin/fastqc"

# conda install -c bioconda multiqc=1.7
MULTIQC = "~/miniconda3/envs/snakepipes_fastqc-multiqc/bin/multiqc"





# --------------------------------------------------------------->>>>>>>
# vars
# --------------------------------------------------------------->>>>>>>
SAMPLES = [
 'M1-1',
 'M6-1',
 'M9-Y-1',
 'S334-1',
 'Ed',
 'M3-2',
 'V-A',
 'M5-2',
 'B-2',
 'M5-1',
 'M4-1',
 'M9-Y-2',
 'Y-1',
 'S334-2',
 'M7-1',
 'V-D',
 'Y-2',
 'EH-2',
 'M6-2',
 'B-1',
 'H1',
 'V-B',
 'M7-2',
 'M2-2',
 'M8-B-2',
 'M1-2',
 'M4-2',
 'M8-B-1',
 'EH-1',
 'M3-1',
 'M2-1']
# SAMPLES = ['test']
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule all
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule all:
    # 有点特殊，输出和输入文件名只能有R1.fastq.gz和_fastqc.html的区别，前面不能有区别！要改就得全改！
    input:
        expand("../fastq/TargetSeq-{sample}_R1.fastq.gz",sample=SAMPLES),
        expand("../fastq/TargetSeq-{sample}_R2.fastq.gz",sample=SAMPLES),
        expand("../qc/fastqc/TargetSeq-{sample}_R1_fastqc.html", sample=SAMPLES),
        expand("../qc/fastqc/TargetSeq-{sample}_R2_fastqc.html", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"
# ------------------------------------------------------------------------------------------>>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------------------------------>>>>>>>>>>
rule fastqc: 
    input: 
        "../fastq/TargetSeq-{sample}_R1.fastq.gz",
        "../fastq/TargetSeq-{sample}_R2.fastq.gz"
    output: 
        "../qc/fastqc/TargetSeq-{sample}_R1_fastqc.html",
        "../qc/fastqc/TargetSeq-{sample}_R2_fastqc.html"
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
        expand(["../qc/fastqc/TargetSeq-{sample}_R1_fastqc.html",
                "../qc/fastqc/TargetSeq-{sample}_R2_fastqc.html"], sample=SAMPLES)
                # the suffix XXX_fastqc.zip is necessary the same with SAMPLES raw name suffix, for multiqc to find the file. 
    output:
        "../qc/multiqc/multiqc_report.html"
    log:
        "../qc/multiqc.log"
    shell: 
        """
        {MULTIQC} ../qc -o ../qc/multiqc --no-data-dir 2>{log}
        """