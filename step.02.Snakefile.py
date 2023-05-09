# ——————————————————>>>>>>>>>>
# Project Name: FASTQC and MULTIQC
# Author: Hua-nan ZHAO
# E-mail: hermanzhaozzzz@gmail.com
# Update log:
#     2022-08-22: start project
# ——————————————————>>>>>>>>>>
import os
import json
# ------------------------------------------------------------------->>>>>>>>>>
# FUNCTIONS
# ------------------------------------------------------------------->>>>>>>>>>
def print_head(SAMPLES, MODE):
    print('----------\nSAMPLES:')
    [print('\t' + i) for i in SAMPLES]
    print('----------\nMODE:')
    print('\t' + MODE)
    print('----------\n\n')

def check_cmd(x):
    return any(
        os.access(os.path.join(path, x), os.X_OK) 
        for path in os.environ["PATH"].split(os.pathsep)
    )

def check_read(x):
    if x == "PE":
        read = ['R1', 'R2']
    elif x == "SE":
        read = ['SE']
    else:
        raise ValueError()
    return read
# ------------------------------------------------------------------->>>>>>>>>>
# SAMPLE INFO
# ------------------------------------------------------------------->>>>>>>>>>
with open('./samples.json') as f:
    dt = json.loads(f.read())

SAMPLES = dt['samples']
MODE = dt['seq_mode']
THREAD = dt['thread']
READ = check_read(MODE)

print_head(SAMPLES, MODE)
print(READ)
# ------------------------------------------------------------------->>>>>>>>>>
# RUN INFO
# ------------------------------------------------------------------->>>>>>>>>>
# THREAD = os.cpu_count() - 1
# ------------------------------------------------------------------->>>>>>>>>>
# DATABASE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# None
# ------------------------------------------------------------------->>>>>>>>>>
# SOFTWARE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# check if cmd exists
assert check_cmd("fastqc")
assert check_cmd("multiqc")
# manually set cmd path
FASTQC = "fastqc"
MULTIQC = "multiqc"

# ------------------------------------------------------------------->>>>>>>>>>
# rule all
# ------------------------------------------------------------------->>>>>>>>>>
rule all:
    input:
        expand("../fastq/{sample}_%s.fastq.gz" % READ[0], sample=SAMPLES),
        expand("../qc/fastqc/{sample}", sample=SAMPLES),
        "../qc/multiqc/multiqc_report.html"

# ------------------------------------------------------------------->>>>>>>>>>
# rule fastqc
# ------------------------------------------------------------------->>>>>>>>>>
rule fastqc: 
    input: 
        "../fastq/{sample}_%s.fastq.gz" % READ[0]
    output: 
        directory("../qc/fastqc/{sample}")
    params:
        SE="../fastq/{sample}_SE.fastq.gz",
        R1="../fastq/{sample}_R1.fastq.gz",
        R2="../fastq/{sample}_R2.fastq.gz"
    log:
        "../qc/fastqc/{sample}.log"
    shell:
        """
        mkdir -p {output}
        echo {input}
        INPUT={input}
        [[ "{input}" =~ .*SE.fastq.gz$ ]] &&
        # if true
        echo "find SE reads!"
        {FASTQC} -o {output} -t {THREAD} {params.SE} > {log} 2>&1 ||
        # if false
        echo "find PE reads!"
        {FASTQC} -o {output} -t {THREAD} {params.R1} {params.R2} > {log} 2>&1
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