import numpy
import random
import os
import sys

def gen_histo(vector, nbins=1, increment = 0, compress = True):
    rows, columns = os.popen('stty size', 'r').read().split()
    max_v = max(vector)
    bin_size = (max_v)/nbins
    bins,edges = numpy.histogram(vector, bins=nbins) 
    edges = [str(edges[i])+' - '+str(edges[i+1])+':' for i in xrange(len(edges)-1)]
    max_edge = max([len(edge) for edge in edges])
    sum_b = numpy.sum(bins)
    bins = numpy.float32(bins)
    bins /= sum_b
    bins *= (int(columns)-max_edge)
    bins = numpy.int32(bins)
    bins += increment
    bins = ['*'*b for b in bins]
    print_columns(edges, bins)

def print_columns(*args):
    max_lengths = [0] + [max([len(str(x)) for x in arg]) for arg in args] + [0]
    for i in xrange(len(args[0])):
        for j in xrange(len(args)):
            print args[j][i], ' '*(max_lengths[j+1]-len(str(args[j][i]))),
        print

def main(argv):
    example = [random.normalvariate(1, .5) for x in xrange(1000000)]
    gen_histo(example,20, 1, False)
    
if __name__ == '__main__':
    main(sys.argv[1:])
