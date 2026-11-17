# Extract-fasta-sequence-from-blast-db-sequences-based-on-blast-outfmt6-file
Extract fasta sequence from blast db sequences based on blast outfmt6 file
**How to use**
`python3 extract_blasthit.py --multifasta ${YOUR FASTA FILE PATH USED FOR MAKING BLAST DB} --out ${OUTPUT FILE NAME} --outfmt6 ${blastn outfmt6 file} --length ${sequence length threshold if you wanna extract the sequences longer than 100bp, please set 100. If you wanna extract all, please set --length 0}`
