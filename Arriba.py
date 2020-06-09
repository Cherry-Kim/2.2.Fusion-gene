import os

STAR_INDEX_DIR='/home/program/arriba_v1.2.0/STAR_index_hs37d5_GENCODE19/'
ANNOTATION='/home/program/arriba_v1.2.0/GENCODE19.gtf'
ASSEMBLY_FA='/home/program/arriba_v1.2.0/hs37d5.fa'
BLACKLIST_TSV='/home/program/arriba_v1.2.0/database/blacklist_hg19_hs37d5_GRCh37_2018-11-04.tsv.gz'
READ1='/home/DATA/Drug/RNA-seq/Sample_MEF1/MEF1_1.fq.gz'
READ2='/home/DATA/Drug/RNA-seq/Sample_MEF1/MEF1_2.fq.gz'
THREADS='16'

os.system('/home/program/arriba_v1.2.0/run_arriba.sh '+STAR_INDEX_DIR+' '+ASSEMBLY_FA+' '+fa+' '+BLACKLIST_TSV+' '+READ1+' '+READ2+' '+THREADS)
#os.system('/home/program/arriba_v1.2.0/run_arriba.sh '+STAR_index+' '+gtf+' '+fa+' '+blacklist+' '+sample+'_1.fq.gz '+sample+'_2.fq.gz 16')
