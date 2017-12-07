This program accepts the user location and returns the closest five events from a list of sample events. The location of these events are randomly generated in this program to be between -10 & +10 on the world. This example takes into account the fact that there could be no tickets left at an event but does not have a time of the event. This assumes all the events are now. This program allows for multiple events at the same location. If I were to change this event for a larger amount of events, I would divide the events into sections by location and only look at the closer selections until we have the 5 events we need.


How to Run the Program:

Need python 2.7

python tickets.py

Sample Output:

Please Input Coordinates 
2,3
Event 2 - $3.00, Distance 1.41421356237
Event 5 - $2.00, Distance 7.07106781187
Event 6 - $10.00, Distance 7.28010988928
Event 4 - $30.00, Distance 8.54400374532
Event 1 - $3.04, Distance 8.94427191