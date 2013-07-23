histo_plot
==========

Simple python function to print a histogram to the shell. Not many features right now, but gets the job done in most cases.

For an example, run histo.py with no arguments to print out a normal distribution. 

Otherwise, import and use gen_histo. Requires numpy.

gen_histo(vector, nbins = 1, increment = 0, compress = True)

vector: vector of numbers, used to generate histogram
nbins: number of bins to use in histogram
increment: increment count for bins (make zeros non-zero for visual purposes)
compress: ignore zero-count bins when printing

Example: python histo.py

Output:
```
-1.48471108563 - -1.24473249187:     *                       
-1.24473249187 - -1.00475389811:     *                       
-1.00475389811 - -0.764775304358:    *                       
-0.764775304358 - -0.524796710601:   *                       
-0.524796710601 - -0.284818116845:   *                       
-0.284818116845 - -0.0448395230885:  **                      
-0.0448395230885 - 0.195139070668:   *****                   
0.195139070668 - 0.435117664424:     **********              
0.435117664424 - 0.675096258181:     ****************        
0.675096258181 - 0.915074851937:     **********************  
0.915074851937 - 1.15505344569:      *********************** 
1.15505344569 - 1.39503203945:       ********************    
1.39503203945 - 1.63501063321:       **************          
1.63501063321 - 1.87498922696:       ********                
1.87498922696 - 2.11496782072:       ****                    
2.11496782072 - 2.35494641448:       **                      
2.35494641448 - 2.59492500823:       *                       
2.59492500823 - 2.83490360199:       *                       
2.83490360199 - 3.07488219575:       *                       
3.07488219575 - 3.3148607895:        *    
```
