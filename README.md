*DESCRIPTION* This program accepts FASTQ files in gzip format as input and reports on the file with the best quality.
				It reports on data such as: number of reads, average length of sequence, the number of sequence duplicates,
				the number of reads that contain undefined (N) nucelotides, the percentage of GC content per sequence,
				and the average undefined percentage per sequence.

*USAGE* When running the program, provide the name of the gzip file, or absolute path to the file, and run. The program will report
		results on the best file. The default input number is three. This will likely be changed in the future. Ammend the
		program to allow input for however many files you wish to use.

*REQUIREMENTS* At least 1GB of memory is recommended. This program does not use any Python packages outside of the standard
			   included.
