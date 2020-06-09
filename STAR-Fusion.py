import os

genome_lib_dir='/home/program/STAR-Fusion/Mouse_gencode_M24_CTAT_lib_Apr062020.plug-n-play/ctat_genome_lib_build_dir/'

sample='/home/DATA/Drug/RNA-seq/Sample1/sample1'
output='/home/DATA/Drug/RNA-seq/Sample1/STAR-Fusion_results/'
os.system('/home/program/STAR-Fusion/STAR-Fusion --genome_lib_dir '+genome_lib_dir+' --left_fq '+sample+'_1.fq.gz  --right_fq '+sample+'_2.fq.gz --output_dir '+output)
