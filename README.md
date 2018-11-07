#Optimal Path Search
(Uninformed Search/ Informed Search)

I have implemented a search algorithm that can find a optimal route between any two cities. For the detail of the cities check Figure1.jpg. The program will take the command line arguments as follows:

find_route uninf/inf input_filename origin_city destination_city heuristic_filename

An example command line is:

python findou uninf input1.txt Munich Berlin  
python findou inf input1.txt Munich Berlin h_kassel.txt

Note that, input1.txt describes road connections between cities in some part of the world shown in Figure1. h_kassel.txt will give us the heuristic value for every state (assuming Kassel is the goal). 

