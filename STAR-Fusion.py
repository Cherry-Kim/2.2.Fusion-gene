import os

genome_lib_dir='/home/program/STAR-Fusion/Mouse_gencode_M24_CTAT_lib_Apr062020.plug-n-play/ctat_genome_lib_build_dir/'
'''
sample='/home/DATA/Drug/RNA-seq/Sample_MEF1/MEF1'
output='/home/DATA/Drug/RNA-seq/Sample_MEF1/STAR-Fusion_results/'

os.system('/home/program/STAR-Fusion/STAR-Fusion --genome_lib_dir '+genome_lib_dir+' --left_fq '+sample+'_1.fq.gz  --right_fq '+sample+'_2.fq.gz --output_dir '+output)
'''

sample2='/home/DATA/Drug/RNA-seq/Sample_RAW_LPS3/RAW_LPS3'
output2='/home/DATA/Drug/RNA-seq/Sample_RAW_LPS3/STAR-Fusion_results/'
os.system('/home/program/STAR-Fusion/STAR-Fusion --genome_lib_dir '+genome_lib_dir+' --left_fq '+sample2+'_1.fq.gz  --right_fq '+sample2+'_2.fq.gz --output_dir '+output2)

sample3='/home/DATA/Drug/RNA-seq/Sample_RAW_Poly4/RAW_Poly4'
output3='/home/DATA/Drug/RNA-seq/Sample_RAW_Poly4/STAR-Fusion_results/'
os.system('/home/program/STAR-Fusion/STAR-Fusion --genome_lib_dir '+genome_lib_dir+' --left_fq '+sample3+'_1.fq.gz  --right_fq '+sample3+'_2.fq.gz --output_dir '+output3)
