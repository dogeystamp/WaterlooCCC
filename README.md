## WaterlooCCC
Solutions to the Waterloo Canadian Computing Competition (CCC) from the CEMC. These are written in Python.<br/>
I'm working on putting all my successful solutions 2010 to 2020 here.<br/>
<br/>
#Common terms used<br/>
For best understanding of the code, here are some terms to know.<br/>
Bold words in the definitions are also defined here.<br/>
These are not in alphabetical order, instead, it's sorted by basic to complicated,<br/>
so you can read in order to understand everything correctly.<br/>
Search using Ctrl-F, because of the way this is sorted, the entry should be the first result<br/>
    Vertex/Vertices: See **Graph**<br/>
    Edge: See **Graph**<br/>
    Edge Weight: See **Graph**<br/>
    Adjacency list: See **Graph**<br/>
    Adjacency Matrix: See **Graph**<br/>
    Graph:<br/>
        A data structure consisting of points, connected to eachother with lines, making a network.<br/>
        The points are called verttices, and the lines are called edges.<br/>
        Sometimes, the edges have "weights", or costs for going over it.<br/>
        This makes it like a road network, with vertices being cities, edges being roads, and weights being the <br/>fuel cost for going over them.<br/>
<br/>
        To implement one:<br/>
            Adjacency list:<br/>
                Make an array. This array's length is the number of vertices in your graph.<br/>
                For every vertex included in the array, there's a list of connected vertices, or edges, if you <br/>prefer.<br/>
            Adjacency Matrix:<br/>
                It's a square matrix, with the number of vertices as side length.<br/>
                Every point is either 1, or 0.<br/>
                If a point is 1, and it's coordinates are x,y, it means vertices x and y are connected.<br/>
                If it's a 0, it's not.<br/>
        You'll see I prefer doing adjacency lists.<br/>
<br/>
    Root: See **Tree**<br/>
    Parent: See **Tree**<br/>
    Child: See **Tree**<br/>
    Tree:<br/>
        It's a **graph**, but there's only ONE way to get from one place to another without going on<br/>
        the same vertex twice. It's thus much simpler and organised.<br/>
        In trees, vertices are called "nodes"<br/>
        Also, there's a parent-child relationship.<br/>
        Here, for example, 2 is child of 1 and parent of 4 and 5.<br/>
        The root is the node with no parents, only children.<br/>
        A good way to think about it is to think of your file system, consisting of files and folders,<br/>
        or a family tree. You could even think of a regular tree, with 1 as the trunk ands the bottom=most layers <br/>as leaves.
        Example:<br/>
            1<br/>
           /\<br/>
          2  3<br/>
         /\  /\<br/>
         4 5 6 7<br/>
<br/>
    Queue:<br/>
        Just like you would think, it's like a waiting line. You serve the one first in line.<br/>
<br/>
    Breadth First Search (BFS):<br/>
        It's an algorithm to go through a **tree** or **graph**.<br/>
        It's suitable for finding the shortest path from one point to another,<br/>
        because the moment you find the destination, you *know* that it's the shortest path to it.<br/>
        This is the order it goes through it:<br/>
            1<br/>
           /\<br/>
          2  3<br/>
         /\  /\<br/>
         4 5 6 7<br/>
        Instructions for executing it:<br/>
            We have a list of places we want to go to, a **queue**.<br/>
            We also have a list of already visited places. We will call this the Visited List.<br/>
            At first, the queue has only one coordinate or place: the start.<br/>
            While the queue isn't empty, remove the first item from the queue (normally using pop() in Python)<br/>
            This item should be conserved in a variable. Let's call it V for vertex.<br/>
            If V is your destination, stop the algorithm.<br/>
            Make sure it isn't in the Visited List. If it is, skip to the next loop.<br/>
            Add V to the Visited List.<br/>
            See what V links to in your tree or graph, then add those to your queue.<br/>