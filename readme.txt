Created by: Akash Lohani 1001661458
Language: Python 2.7

How the code is structured: 

*Abstract
 	This software computes the optimal route between the origin city and the destination city using uninformed search and informed search.
	Uniformed cost search is performed by uniform cost serach.
	Informed cost search is performed by A* search.

*Argument
	Argument to run the program takes as follows.
	Uninformed search "python find_route.py input1.txt (origin city) (destination city)"
	Informed search  "python find_route.py input1.txt (origin city) (destination city) h_kassel.txt"

*Search method selection 
	Search method selection is done by length of arguments.
	
* Uninformed search
	1.Read input1.txt; describes road connections between cities in some part of the world
	2.Read Origin(Random) Destination(Random)
	3.Uniform cost search performed using heapq
	4.Graph Search applied using closed set(logging the city visited).



*Informed search
	1.Read input1.txt; describes road connections between cities in some part of the world
	2.Read Origin(Random) Destination(Kassel)
	3.Read h_kassel.txt; heauristics of the euqlid distance from each city to Kassel
	4.A* search performed using heapq
	5.Graph Search applied using closed set(logging the city visited).

***Result***

*Uninformed search
(Bremen-Kassel)
nodes expanded: 12
distance: 297km
route:
Bremen to Hannover, 132km
Hannover to Kassel, 165km

(London-Kassel)
nodes expanded: 7
distance: infinity
route:

*Informed search
(Bremen-Kassel)
nodes expanded: 3
distance: 297km
route:
Bremen to Hannover, 132km
Hannover to Kassel, 165km

(London-Kassel)
nodes expanded: 7
distance: infinity
route:


Instructions
1. Change directory to the place you saved my file.
2. Make sure input1.txt and h_kassel.txt is in the same directory with find_route.py.
3. Type argument stated above. Make sure to put "python" in the very beginning of the argument.
4. Tested in the following environment.
	1. Windows10 python2.7
	2. Omega Server python2.4
5.Thanks for reading.


	