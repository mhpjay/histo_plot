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

Output: 

-1.3280483031 - -1.07939910003:      *                        
-1.07939910003 - -0.830749896958:    *                        
-0.830749896958 - -0.582100693886:   *                        
-0.582100693886 - -0.333451490814:   *                        
-0.333451490814 - -0.0848022877428:  **                       
-0.0848022877428 - 0.163846915329:   ****                     
0.163846915329 - 0.4124961184:       *********                
0.4124961184 - 0.661145321472:       ****************         
0.661145321472 - 0.909794524544:     **********************   
0.909794524544 - 1.15844372762:      ************************ 
1.15844372762 - 1.40709293069:       *********************    
1.40709293069 - 1.65574213376:       **************           
1.65574213376 - 1.90439133683:       ********                 
1.90439133683 - 2.1530405399:        ****                     
2.1530405399 - 2.40168974297:        *                        
2.40168974297 - 2.65033894604:       *                        
2.65033894604 - 2.89898814912:       *                        
2.89898814912 - 3.14763735219:       *                        
3.14763735219 - 3.39628655526:       *                        
3.39628655526 - 3.64493575833:       * 
