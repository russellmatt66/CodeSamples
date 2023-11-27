parsePerfStat.py/
- Python script to parse the output from a call, or set of calls, of `perf stat` with the hardware code for talking to the floating-point arithmetic counter.
- Calculates mean, and standard deviation of the dataset of program wall-times.

parsePerfData.py/
- Reads through directory of files containing `perf stat -e` output from espic_1d1v run.
- Creates .csv file that contains the execution time statistics, and amount of arithmetic performed, for each N,Nx pair.

CollectPerfData.py/
- Wraps around `perf_data.sh` 
- Automates creation of data files from running `perf stat -e`