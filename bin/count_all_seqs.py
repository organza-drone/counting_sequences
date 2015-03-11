#!/usr/bin/env python

import sys
import os
import os.path
import fnmatch
#home-made library
import seq_utils

if len(sys.argv) < 2:
    sys.exit("\nUsage: count_all_seqs.py <input_directory>\n")

directory       = sys.argv[1]
directory_list  = sorted(os.listdir(directory))

for filename in directory_list:
    input_file = open(os.path.join(directory, filename))

    if fnmatch.fnmatch(filename, '*.fasta'):
        print filename, seq_utils.count_seqs(input_file)
