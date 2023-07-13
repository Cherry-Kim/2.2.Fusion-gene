# Arriba 

https://arriba.readthedocs.io/en/v1.1.0/quickstart/)https://arriba.readthedocs.io/en/v1.1.0/quickstart/

wget https://github.com/suhrig/arriba/releases/download/v1.1.0/arriba_v1.1.0.tar.gz

tar -xzf arriba_v1.1.0.tar.gz

cd arriba_v1.1.0 && make

#
#Available assemblies and annotations: hg19+GENCODE19 GRCh37+GENCODE19 hs37d5+GENCODE19 hg38+ENSEMBL93 GRCh37+RefSeq hs37d5+RefSeq GRCh38+GENCODE28 hg19+ENSEMBL87 hg19+RefSeq hg38+RefSeq GRCh38+RefSeq GRCh37+ENSEMBL87 hs37d5+ENSEMBL87 hg38+GENCODE28 GRCh38+ENSEMBL93

./download_references.sh GRCh38+ENSEMBL93 

#ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

#ftp://ftp.ensembl.org/pub/release-93/gtf/homo_sapiens/Homo_sapiens.GRCh38.93.chr.gtf.gz
