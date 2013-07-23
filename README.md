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

-1.35330875828 - -1.12303859386:    *                       
-1.12303859386 - -0.892768429437:   *                       
-0.892768429437 - -0.662498265016:  *                       
-0.662498265016 - -0.432228100595:  *                       
-0.432228100595 - -0.201957936174:  *                       
-0.201957936174 - 0.0283122282472:  ***                     
0.0283122282472 - 0.258582392668:   ******                  
0.258582392668 - 0.488852557089:    ***********             
0.488852557089 - 0.71912272151:     *****************       
0.71912272151 - 0.949392885931:     *********************   
0.949392885931 - 1.17966305035:     *********************** 
1.17966305035 - 1.40993321477:      *******************     
1.40993321477 - 1.64020337919:      *************           
1.64020337919 - 1.87047354361:      ********                
1.87047354361 - 2.10074370804:      ****                    
2.10074370804 - 2.33101387246:      **                      
2.33101387246 - 2.56128403688:      *                       
2.56128403688 - 2.7915542013:       *                       
2.7915542013 - 3.02182436572:       *                       
3.02182436572 - 3.25209453014:      *                       
