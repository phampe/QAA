#!/bin/bash

#SBATCH --account=bgmp   ### change this to your actual account for charging
#SBATCH --partition=bgmp       ### queue to submit to
#SBATCH --job-name=Petersjob    ### job name
#SBATCH --output=peter_output_%j.out   ### file in which to store job stdout. j holds the job id
#SBATCH --error=hostname_%j.err    ### file in which to store job stderr
#SBATCH --time=0-03:00:00                ### wall-clock time limit, in minutes
#SBATCH --nodes=1               ### number of nodes to use
#SBATCH --cpus-per-task=8       ### number of cores for each task
dir="/projects/bgmp/ppham4/bioinfo/Bi621/PS/PS8"
#conda activate bgmp_py310
conda activate QAA

# /usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
#     --outFilterMultimapNmax 3 \
#     --outSAMunmapped Within KeepPairs \
#     --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
#     --readFilesCommand zcat \
#     --readFilesIn "/projects/bgmp/shared/Bi621/dre_WT_ovar12_R1.qtrim.fq.gz" "/projects/bgmp/shared/Bi621/dre_WT_ovar12_R2.qtrim.fq.gz" \
#     --genomeDir "/projects/bgmp/ppham4/bioinfo/Bi621/PS/PS8/Danio_rerio.GRCz11.dna.ens104.STAR_2.7.1a" \
#     --outFileNamePrefix align/star_alignment
#     ### this is tabbed in so that it is easily read.


/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
    --outFilterMultimapNmax 3 \
    --outSAMunmapped Within KeepPairs \
    --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
    --readFilesCommand zcat \
    --readFilesIn "/projects/bgmp/ppham4/bioinfo/Bi623/work/cutadapt_trimmomatic/forwar_pair_fox.gz" "/projects/bgmp/ppham4/bioinfo/Bi623/work/cutadapt_trimmomatic/reverse_pair_fox.gz" \
    --genomeDir "/projects/bgmp/ppham4/bioinfo/Bi623/work/Star/mouse.107.STAR" \
    --outFileNamePrefix fox
    ### this is tabbed in so that it is easily read.