# node clustering
Individual project

# 1. Justification of why you have chosen your topic.
The topic is associated with the uav trajectory problem which is typically solved through two steps: clustering nodes and planning the shortest path covering the clusters.  
There is an assumption that it is desired that the number of cluster should be as small as possible.
# 2. What is the topic?
The topic is grouping K nodes into N clusters, where N is no more than a given integer number, M. This can be coverted into a set covering problem.  
The nodes can be grouped into cluster if they all locate within radius r of the point with the XY-coordinate that is the geometric mean of those nodes' XY-coordinates.  
# 3. Design decision explaining why you select:
## 3.1. Parameters such as the size of an initial population.
The number of the nodes: K  
The size of population, P: [1000, inif), 1000 (R: Larger population can acelerate the convergence of the algorithm at the expense of time cost);  
The probability of mutation: [0, 0.5], 0.2 (R: If more than 0.5, the algorithm is the same as the random strategy);  
The round of crossover: [P/2, P], P (R: More offsprings can acelerate the convergence of the algorithm at the expense of time cost);  
The maximum number of clusters: N <= K (R: we should consider the worst case that nodes are significantly far from each other)  
The individual: an array with the size of K  
The radius, r: 100 (R: it is not determined yet)  
The maximum interval interval between two generation where best-so-far result occurs, Max_inter: 1000.  

The individual example (5 nodes):
|node ID|1|2|3|4|5|
|-|-|-|-|-|-|
|Implication value of cluster center|0|0|1|0|1|

## 3.2. Stopping criteria.
The interval between two generation where best-so-far result occurs is more than Max_inter.
## 3.3. Fitness function.
![image](https://github.com/MRMRMRMAY/Advanced-Software-Analysis-202102/blob/main/fitness2.png)
w_i is the node in the cluster i.  
c_j is the center of cluster j.  
r is the redius of the circle shaped cluster.  
1{.} is indicate function  
||a,b|| is the euclidean distance between the point a and b.
## 3.4. Selection operator.
if the population is large: tournament selection  
otherwise: roulette wheel sampling OR stochastic sampling  
## 3.5. Crossover operator.
Double points crossover  
## 3.6. Mutation operator.
Single point mutation: randomly select two positions on the individual and swap their values.  
## 3.7. Generational selection strategy.
elitist selection: Select top-P best individuals including offsprings in the current generation as the population of the next generation.
# 4. How to run your project.
Load the probject using pychrom, execute the file "main.py"
# 5. How to adjust parameters.
