# !/usr/bin/env python3
from statistics import mean
import gzip


def qa_analysis(filename):
    with gzip.open(filename, 'r') as fastq:
        strands = fastq.readlines()[1::4]
    strands = [strand.decode('utf8').rstrip() for strand in strands]
    lengths = [len(strand) for strand in strands]
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


archive1 = qa_analysis((input()))
archive2 = qa_analysis((input()))
archive3 = qa_analysis((input()))
archives_list = [archive1, archive2, archive3]
lowest_n_read = min(x['reads_with_n'] for x in archives_list)
for x in archives_list:
    if x['reads_with_n'] == lowest_n_read:
        best_archive = x

print(f'Reads in the file = {best_archive["reads"]}:')
print(f'Reads sequence average length = {best_archive["avg_length"]}\n')
print(f'Repeats = {best_archive["repeats"]}\nReads with Ns = {best_archive["reads_with_n"]}\n')
print(f'GC content average = {best_archive["avg_gc_content"]}%')
print(f'Ns per read sequence = {best_archive["Ns_per_read"]}%')
