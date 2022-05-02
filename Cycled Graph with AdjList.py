# Khaoula Ait Soussi: 79155

"""This program reads from an input file the the number of vertices, the number of edges, and edges of the graph.
It uses an adjacency list as a data structure to represent the graph, and checks whether the graph is cycled over all its vertices"""

# This is to read the text file as an array of lines
with open('inp.txt', 'r') as file:
  Lines = file.readlines()

# Read the number of vertices from the first line of the file/array
verts = eval(Lines[0])

# Read the number of edges from the second line of the file/array
edges = eval(Lines[1])

# Create an adjacency list that has empty rows. The number of rows is the number of vertices
# Here the index of each row represents a vertex, and each row represents the adjacency list of that vertex
adjLst = [list() for i in range(verts)]

# Fill in the adjacency list while asking the user for edges in the format a b
for i in range(2, len(Lines)):
  a,b = Lines[i].split(" ")
  a = eval(a)
  b = eval(b)
  # Whenever an edge is read from the file/array, we append its vertices to the corresponding rows in the adjacency list
  adjLst[a-1].append(b-1)   
  adjLst[b-1].append(a-1)

# Rule out other obvious non-cycled graphs
# Graphs that have at least one vertex that doesn't have degree 2
# We check for this by looking at the number of columns of each row in the adjacency list
deg2flag = True
for i in range(verts):
  if(len(adjLst[i]) != 2):
    print("The graph is not cycled because at least one vertex doesn't have degree 2!")
    deg2flag = False
    break

# If each vertex has degree 2, we check if the graph is one big cycle or composed of smaller cycles
if(deg2flag == True):
  cycleclosed = False
  prev_ver = 0
  visited_ver = 1
  # The next and current vertex is the first one adjacent to vertex 0
  next_ver = adjLst[0][0]   
  current_ver = adjLst[0][0]  
  while(cycleclosed == False):
    for i in range(2):  # we know that each row has only two columns (each vertex is of degree 2)
      if(adjLst[current_ver][i] != prev_ver):
        next_ver = adjLst[current_ver][i]
        break
    visited_ver = visited_ver + 1
    prev_ver = current_ver
    current_ver = next_ver
    if(current_ver == 0):
      cycleclosed = True

  # Once the cycle is closed, we need to check if all the vertices have been traversed
  if(visited_ver == verts):
    print("The graph is cycled! ")
  else:
    print("The graph is not cycled! It is composed of smaller cycled graphs.")
