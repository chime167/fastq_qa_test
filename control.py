# !/usr/bin/env python3
from statistics import mean
import gzip
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filenames', nargs='*', help='Enter the filenames or path to files')
args = parser.parse_args()

def qa_analysis(filename):
    with gzip.open(filename, 'r') as fastq:
        strands = fastq.readlines()[1::4]
    strands = [strand.decode('utf8').rstrip() for strand in strands]
    lengths = [*map(len, strands)]
    gc_counts = [((strand.count('G') + strand.count('C')) / length * 100) for strand, length in zip(strands, lengths)]
    n_perc = [(strand.count('N') / length * 100) for strand, length in zip(strands, lengths)]
    repeats = len(strands) - len(set(strands))
    n_strands_count = len([strand for strand in strands if 'N' in strand])
    reads = len(strands)
    avg_length = round(mean(lengths))
    avg_gc_content = round(mean(gc_counts), 2)
    n_per_read_seq = round(mean(n_perc), 2)
    return {'reads': reads, 'avg_length': avg_length, 'repeats': repeats, 'reads_with_n': n_strands_count,
            'avg_gc_content': avg_gc_content, 'Ns_per_read': n_per_read_seq}



def main():
    '''Program that reports stats on the content of compressed FASTQ files
    CLI parameter: filenames - just enter the names of the compressed FASTQ files you wish to analyze
    The program reports:
        -Number of reads
        -Average sequence length
        -Number of repeats
        -Reads with Ns (unknowns)
        -Average GC content
        -Average Ns per read sequence'''
    archives_list = [qa_analysis(file) for file in args.filenames]

    for read in archives_list:
        print(f'Reads in the file = {read["reads"]}:')
        print(f'Reads sequence average length = {read["avg_length"]}\n')
        print(f'Repeats = {read["repeats"]}\nReads with Ns = {read["reads_with_n"]}\n')
        print(f'GC content average = {read["avg_gc_content"]}%')
        print(f'Ns per read sequence = {read["Ns_per_read"]}%')
    

if __name__ == '__main__': main()
