import os

# ------------------------------------------------------------------->>>>>>>>>>
# Author: Herman ZHAO
# Email: hermanzhaozzzz@gmail.com
# Update
#     date: 2021-07-26 log: format annotation and software path
# ------------------------------------------------------------------->>>>>>>>>>

# ------------------------------------------------------------------->>>>>>>>>>
# SAMPLE INFO
# ------------------------------------------------------------------->>>>>>>>>>
SAMPLES = [
    'ABE-HEK4-rep1_combined',
    'ABE-HEK4-rep2_combined',
    'ABE8e-HEK4-rep1_combined',
    'ABE8e-HEK4-rep2_combined',
    'ACBE-HEK4-rep1_combined',
    'ACBE-HEK4-rep2_combined',
    'CBE-HEK4-rep1_combined',
    'CBE-HEK4-rep2_combined'
]

# ------------------------------------------------------------------->>>>>>>>>>
# RUN INFO
# ------------------------------------------------------------------->>>>>>>>>>
THREADS = '24'

# ------------------------------------------------------------------->>>>>>>>>>
# DATABASE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# none

# ------------------------------------------------------------------->>>>>>>>>>
# SOFTWARE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# get the application path
with os.popen("which fastqc") as path:
    FASTQC = path.read().strip()
    print('PATH fastqc:', FASTQC)
with os.popen("which multiqc") as path:
    MULTIQC = path.read().strip()
    print('PATH multiqc:', MULTIQC)

if "" in [FASTQC, MULTIQC]:
    raise ValueError("The necessary software path is missing!!!")
else:
    print("pass software check...\n")


# ------------------------------------------------------------------->>>>>>>>>>
# rule all
# ------------------------------------------------------------------->>>>>>>>>>
rule all:
    input:
        expand("../fastq/{sample}_R1.fastq.gz", sample=SAMPLES),
        expand("../fastq/{sample}_R2.fastq.gz", sample=SAMPLES),
        expand("../qc/fastqc/{sample}", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"

# ------------------------------------------------------------------->>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------->>>>>>>>>>
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

# ------------------------------------------------------------------->>>>>>>>>>
# rule multiqc
# ------------------------------------------------------------------->>>>>>>>>>
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