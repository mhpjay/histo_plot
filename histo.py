import numpy
import random
import os
import sys

def gen_histo(vector, nbins=1, increment = 0, compress = True, round_label = 0):
    rows, columns = os.popen('stty size', 'r').read().split()
    bins,edges = numpy.histogram(vector, bins=nbins)
    prepend = {1:'+', 0:' ', -1:''}
    if round_label > 0:
        #edges = numpy.round(edges,round_label) 
        rounder_string = "%0."+str(round_label)+'f'
        edges = [prepend[cmp(edges[i],0)]+rounder_string % edges[i]+' to '+prepend[cmp(edges[i+1],0)]+rounder_string % edges[i+1]+':' for i in xrange(len(edges)-1)]
    else:
        edges = [prepend[cmp(edges[i],0)]+str(edges[i])+' to '+prepend[cmp(edges[i+1], 0)]+str(edges[i+1])+':' for i in xrange(len(edges)-1)]
    max_edge = max([len(edge) for edge in edges])
    sum_b = numpy.sum(bins)
    bins = numpy.float32(bins)
    bins /= sum_b
    bins *= (int(columns)-max_edge) #to help with wrapping
    bins = numpy.int32(bins)
    if compress:
        bins_remove = [i for i in xrange(len(bins)) if bins[i] == 0]
        edges = [edges[i] for i in xrange(len(edges)) if i not in bins_remove]
        bins = numpy.array([bins[i] for i in xrange(len(bins)) if i not in bins_remove])
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
    gen_histo(example,20, 1, False, 10)
    gen_histo(example,20, 1, False, 0)
    
if __name__ == '__main__':
    main(sys.argv[1:])
