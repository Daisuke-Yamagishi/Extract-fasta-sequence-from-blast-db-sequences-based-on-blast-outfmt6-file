import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='Extract sequences from outfmt6 info')
parser.add_argument('--outfmt6')
parser.add_argument('--multifasta')
parser.add_argument('--out')
parser.add_argument('--length')
args = parser.parse_args() 
fmt6 = args.outfmt6
fasta = args.multifasta
out = args.out
len = args.length

def extract_by_len(fmt6, len):
    matched = []
    with open(fmt6, 'r') as file:
        for line in file:
            fields = line.rstrip("\n").split("\t")
            print(fields)
            if int(fields[3]) >= int(len):
                matched.append(line)
    return matched
matched = extract_by_len(fmt6, len)
#This is set comprehension. NOT list comprehension. 
#If you use set comprehension instead of set(), 
#the matched_ids will automatically be uniq.
matched_ids = {
    line.rstrip("\n").split("\t")[1]
    for line in matched
    }
matched_records = []
found_ids = set()

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in matched_ids:
        matched_records.append(record)
        found_ids.add(record.id)
        print(matched_records)
        print(found_ids)

with open(out, "w") as output:
    SeqIO.write(matched_records, output, "fasta")