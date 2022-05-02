# Cycled-graph

## Description
This project was part of the assessments assigned in Analysis of Algorithms class with Dr. Naeem Nisar Sheikh.
The program reads from an input file the the number of vertices, the number of edges, and edges of the graph.
It uses an adjacency list as a data structure to represent the graph, and checks whether the graph is cycled over all its vertices.

## Proposed Solution
The program uses an input file to read the number of vertices, the number of edges, and the edges themselves. 
I created three input files to test different cases, and of course you can create another file of yours that has the same format as the other files.
The input file is set by default to inp.txt; if you would like to change it to another file, just change the statement in line 6 with the name of the desired file. 

Here are details about the content of each file: 
inp.txt ==>   
	A bunch of cycles instead of one big Cycle.
inp2.txt ==>
	Big Cycle.
inp3.txt ==>
	The graph is not a cycle because at least one vertex is not of degree 2.
