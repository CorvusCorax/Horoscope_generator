#!/bin/bash
python3 prepare_data.py
cat all.txt |sort -R >all_random.txt
head -n 12500 all_random.txt >train.txt
tail -n +12501 all_random.txt >valid.txt
