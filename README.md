```markdown
## WaterlooCCC
 Solutions to the Waterloo Canadian Computing Competition (CCC) from the CEMC. These are written in Python.
I'm working on puttinng all my successful solutions 2010 to 2020 here.

#Common terms used
For best understanding of the code, here are some terms to know.
Bold words in the definitions are also defined here.
These are not in alphabetical order, instead, it's sorted by basic to complicated,
so you can read in order to understand everything correctly.
Search using Ctrl-F, because of the way this is sorted, the entry should be the first result
    Vertex/Vertices: See **Graph**
    Edge: See **Graph**
    Edge Weight: See **Graph**
    Adjacency list: See **Graph**
    Adjacency Matrix: See **Graph**
    Graph:
        A data structure consisting of points, connected to eachother with lines, making a network.
        The points are called verttices, and the lines are called edges.
        Sometimes, the edges have "weights", or costs for going over it.
        This makes it like a road network, with vertices being cities, edges being roads, and weights being the fuel cost for going over them.

        To implement one:
            Adjacency list:
                Make an array. This array's length is the number of vertices in your graph.
                For every vertex included in the array, there's a list of connected vertices, or edges, if you prefer.
            Adjacency Matrix:
                It's a square matrix, with the number of vertices as side length.
                Every point is either 1, or 0.
                If a point is 1, and it's coordinates are x,y, it means vertices x and y are connected.
                If it's a 0, it's not.
        You'll see I prefer doing adjacency lists.

    Root: See **Tree**
    Parent: See **Tree**
    Child: See **Tree**
    Tree:
        It's a **graph**, but there's only ONE way to get from one place to another without going on
        the same vertex twice. It's thus much simpler and organised.
        In trees, vertices are called "nodes"
        Also, there's a parent-child relationship.
        Here, for example, 2 is child of 1 and parent of 4 and 5.
        The root is the node with no parents, only children.
        A good way to think about it is to think of your file system, consisting of files and folders,
        or a family tree. You could even think of a regular tree, with 1 as the trunk ands the bottom=most layers as leaves.
        Example:
            1
           /\
          2  3
         /\  /\
         4 5 6 7
    Breadth First Search (BFS):
        It's an algorithm to go through a **tree** or **graph**.
        It's suitable for finding the shortest path from one point to another,
        because the moment you find the destination, you *know* that it's the shortest path to it.
        This is the order it goes through it:
            1
           /\
          2  3
         /\  /\
         4 5 6 7
        Instructions for executing it:
            We have a list of places we want to go to, a **queue**.
            We also have a list of already visited places. We will call this the Visited List.
            At first, the queue has only one coordinate or place: the start.
            While the queue isn't empty, remove the first item from the queue (normally using pop() in Python)
            This item should be conserved in a variable. Let's call it V for vertex.
            If V is your destination, stop the algorithm.
            Make sure it isn't in the Visited List. If it is, skip to the next loop.
            Add V to the Visited List.
            See what V links to in your tree or graph, then add those to your queue.
```