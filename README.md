# 标准质控流程
> author: 赵华男 | ZHAO Hua-nan
>
> email: hermanzhaozzzz@gmail.com
>
> [知乎](https://www.zhihu.com/people/hymanzhaozzzz) | [博客](http://zhaohuanan.cc)

## 说明
本snakemake流程用于批量运行单端、双端测序FASTQ文件的质控(fastqc 和 multiqc) 

This snakemake pipeline aims to do quality control for single-end(SE) or paired-end(PE) FASTQ file(fastqc and multiqc)

- 所有测序文件存放目录为`../fastq`
- **只能全部**存放单端或者全部存放双端测序
- 单端测序以`_SE.fastq.gz`结尾
- 双端测序以`_R1.fastq.gz | _R1.fastq.gz`结尾
- Jupyterlab 运行step1 RUN -> Run All Cells 得到`sample.json`，检查样本完整性
- Snakemake 运行step2 得到质控结果，并在 `../qc/multiqc/multiqc_report.html` 中查看汇总结果


## 环境:
```
conda install snakemake fastqc multiqc runipy
```
## 运行
```shell
# Jupyterlab运行step1生成json文件或者命令行运行笔记本
runipy step.01.GetFileName.ipynb
# 测试运行
snakemake -pr -j 10 -s step.02.Snakefile.smk.py -n
# 实际运行
snakemake -pr -j 10 -s step.02.Snakefile.smk.py
```


## 文件树
```shell
ChIP-seq|⇒ tree -L 2
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
│   ├── Spike-in-antibody-only_ChIP-seq_CTCF-AID_untreated_rep2_SE.fastq.gz
│   ├── sra_info.txt
│   ├── SRR5517476.sra
│   ├── SRR5517477.sra
│   ├── SRR5517478.sra
│   ├── SRR5517479.sra
│   ├── SRR5517480.sra
│   ├── SRR5517481.sra
│   ├── SRR5517482.sra
│   ├── SRR5517483.sra
│   ├── SRR5517484.sra
│   └── SRR5517485.sra
└── snakepipes_fastqc-multiqc
    ├── 1
    ├── README.md
    ├── samples.json
    ├── step.01.GetFileName.ipynb
    └── step.02.Snakefile.smk.py

3 directories, 25 files
```


    
