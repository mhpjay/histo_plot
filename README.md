histo_plot
==========

Simple python function to print a histogram to the shell. Useful when working remotely.
Not many features right now, but gets the job done in most cases.

Otherwise, import and use print_histo. Requires numpy.

print_histo(vector, nbins = 1, increment = 0, compress = True, round_increment = 0)

vector: vector of numbers, used to generate histogram  
nbins: number of bins to use in histogram  
increment: increment count for bins (make zeros non-zero for visual purposes)  
compress: ignore zero-count bins when printing  
round_increment: whether or not to round bin labels for cleaner output. Default of 0 means no rounding, must be > 0

Run an example with python histo.py: will show a graph with rounded bins and one without  
Example: python histo.py

Output:
```
-1.4246771621 to -1.1732290880:  *                         
-1.1732290880 to -0.9217810140:  *                         
-0.9217810140 to -0.6703329399:  *                         
-0.6703329399 to -0.4188848658:  *                         
-0.4188848658 to -0.1674367918:  *                         
-0.1674367918 to +0.0840112823:  ***                       
+0.0840112823 to +0.3354593564:  ********                  
+0.3354593564 to +0.5869074304:  ***************           
+0.5869074304 to +0.8383555045:  **********************    
+0.8383555045 to +1.0898035786:  ************************* 
+1.0898035786 to +1.3412516526:  ***********************   
+1.3412516526 to +1.5926997267:  *****************         
+1.5926997267 to +1.8441478008:  **********                
+1.8441478008 to +2.0955958748:  ****                      
+2.0955958748 to +2.3470439489:  **                        
+2.3470439489 to +2.5984920230:  *                         
+2.5984920230 to +2.8499400970:  *                         
+2.8499400970 to +3.1013881711:  *                         
+3.1013881711 to +3.3528362452:  *                         
+3.3528362452 to +3.6042843192:  *                         
-1.42467716209 to -1.17322908803:     *                        
-1.17322908803 to -0.921781013964:    *                        
-0.921781013964 to -0.670332939898:   *                        
-0.670332939898 to -0.418884865833:   *                        
-0.418884865833 to -0.167436791767:   *                        
-0.167436791767 to +0.0840112822982:  ***                      
+0.0840112822982 to +0.335459356364:  ********                 
+0.335459356364 to +0.586907430429:   **************           
+0.586907430429 to +0.838355504495:   *********************    
+0.838355504495 to +1.08980357856:    ************************ 
+1.08980357856 to +1.34125165263:     **********************   
+1.34125165263 to +1.59269972669:     ****************         
+1.59269972669 to +1.84414780076:     *********                
+1.84414780076 to +2.09559587482:     ****                     
+2.09559587482 to +2.34704394889:     **                       
+2.34704394889 to +2.59849202295:     *                        
+2.59849202295 to +2.84994009702:     *                        
+2.84994009702 to +3.10138817108:     *                        
+3.10138817108 to +3.35283624515:     *                        
+3.35283624515 to +3.60428431922:     *  
```


