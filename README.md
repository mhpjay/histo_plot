histo_plot
==========

Simple python function to print a graphical histogram to the shell. Not many features right now, but gets the job done in most cases.

For an example, run histo.py with no arguments to print out a normal distribution. 

Otherwise, import and use gen_histo. Requires numpy.

gen_histo(vector, nbins = 1, increment = 0, compress = True)

vector: vector of numbers, used to generate histogram
nbins: number of bins to use in histogram
increment: increment count for bins (make zeros non-zero for visual purposes)
compress: ignore zero-count bins when printing

Example: python histo.py
