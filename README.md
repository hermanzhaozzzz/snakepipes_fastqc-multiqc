# snakepipes_fastqc-multiqc
## about author

> author: [赵华男 | ZHAO Hua-nan](https://scholar.google.com/citations?user=ojSVoWQAAAAJ&hl=en)
>
> email: hermanzhaozzzz@gmail.com
>
> [Zhihu](https://www.zhihu.com/people/hymanzhaozzzz) | [BLOG](http://zhaohuanan.cc)

## doc
`snakepipes_fastqc-multiqc` is a standard quality control snakemake pipeline for NGS/HTS data
- input file: FASTQ file by NGS sequencing, Single-end (SE) Paired-end (PE) are supported.
- output file:
    - fastqc report
    - multiqc report
- requirement
    - raw FASTQ file must put in `../fastq` directory
    - **only the same** sequencing type (SE or PE) can be assigned into the `sample.json` at once!
    - SE sequencing data must named its suffix -> `_SE.fastq.gz`
    - PE sequencing data must named its suffix -> `_R1.fastq.gz` and`_R2.fastq.gz`
    - run Jupyter notebook to abtain the config for snakemake -> `sample.json`
    - run Snakemake to abtain the QC results at directory -> `../qc`
        - summary html for QC stat -> `../qc/multiqc/multiqc_report.html`


## env:
```
conda env create -f conda_env.yml
```
## run
```shell
# run Jupyter notebook to abtain the config
# run this cmd
# or
# open notebook and run all cells
runipy step.01.GetFileName.ipynb
# 测试运行
snakemake -pr -j 10 -s step.02.Snakefile.smk.py -n
# 实际运行
snakemake -pr -j 10 -s step.02.Snakefile.smk.py
```


## project structure
```shell
tree -L 2 .
.
├── fastq
│   ├── CTCF_ChIP-seq_CTCF-AID_auxin2days_rep1_SE.fastq.gz
│   ├── CTCF_ChIP-seq_CTCF-AID_auxin2days_rep2_SE.fastq.gz
│   ├── CTCF_ChIP-seq_CTCF-AID_untreated_rep1_SE.fastq.gz
│   ├── CTCF_ChIP-seq_CTCF-AID_untreated_rep2_SE.fastq.gz
│   ├── CTCF_ChIP-seq_CTCF-AID_washoff2days_rep1_SE.fastq.gz
│   ├── CTCF_ChIP-seq_CTCF-AID_washoff2days_rep2_SE.fastq.gz
│   ├── Input_for_CTCF_ChIP-seq_CTCF-AID_auxin2days_rep1_SE.fastq.gz
│   ├── Input_for_CTCF_ChIP-seq_CTCF-AID_auxin2days_rep2_SE.fastq.gz
│   ├── Spike-in-antibody-only_ChIP-seq_CTCF-AID_untreated_rep1_SE.fastq.gz
│   └── Spike-in-antibody-only_ChIP-seq_CTCF-AID_untreated_rep2_SE.fastq.gz
└── snakepipes_fastqc-multiqc
    ├── README.md
    ├── samples.json
    ├── step.01.GetFileName.ipynb
    └── step.02.Snakefile.smk.py
```


    
