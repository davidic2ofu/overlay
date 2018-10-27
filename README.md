# Super Peer Overlay Network Simulation

## To the grader:

This program is written in Python 2.7.
Packages networkx and matplotlib are required for graph tools and visual display.


The graph is iniitialized with 100 randomly-placed "real" nodes, each connected to 25% of its
peers.  Once the number of super peers is specified, the program will update the graph such that
the super peer node size will scale up and have a light blue color.  Non-super peers will be color
coded various shades of blue depending on the super peer whose network they belong to in the 
overlay.  For the overlay network, super peers are selected randomly, then peers are assigned to
each super peer based on proximity.


The software should work for all cases:

1. Adding nodes
   - generates new node id
   - generates random position in graph
   - edges are generated connecting new node to 25% of its neighbors
   - super peer assignments are reset
   - returns confirmation of added node to user
2. Deletion of nodes
   - takes node id from user
   - removes node
   - super peer assignments are reset
   - returns confirmation of deleted node to user
3. Request route between real nodes
   - takes origin and destination node id's from user
   - routes shortest path between origin node and its super peer
   - routes shortest path from origin node's super peer to destination node's super peer
   - routes shortest path between destination node's super peer to destination node
   - returns route information to user
4. View super peer tables
   - A list of peers assigned to each super peer is generated
   - list is returned to user


Thank you,
David Rosenberg
U00063482


### Assigned instructions from Dr. Neel

For this assignment, I want you to model an overlay network in simulation. Your simulation must display visually both the "real" network and the overlay. Your simulation must generate at least 100 nodes for the "real" network. Each node of the "real" network must be connected randomly to at least 25% of the other "real" nodes. The overlay network must connect every node in a structured manner using super peers. These super peers would divide the real network into regions such that there would be one super peer per region. The number of super peers is to be entered at runtime and your simulation should permit updates to the number of nodes. Your simulation should allow the user to request a route between real nodes; and your program should output the route between the nodes for both the real and overlay networks. Your simulation should route from source data work node to a super peer near the source to a super peer near the destination to the destination. You are free to use any programming language you like to meet this requirement.

### Other considerations:

Please plan for future assignments to ask you to scale this simulation up to much larger sizes. Also plan to allow for sparesely connected real networks. Also, plan to address the adding and deleting of nodes and super peers.