# Raspberry-Pi-Camera-Project
~~Python project created for the RaspberryPi 2. 

Small project that captures video when the state changes on a pin set, either high or low, and saves that video with a timestamp to an external flash drive plugged into the pi. (The external flash drive section will have to be set up before hand and the save directory changed to the correct for that build) 

The hardware set up consists of a RaspberryPi 2, pi camera, external flash drive, and tripod compatable case. The pins are connected directly to a normally closed or normally open relay. This allows the monitoring of an event and capturing of that event for later review.

Because of the programming, capturing video happens when state changes AND when state returns to its original position. Creating two seperate timestamped videos. This was intended to keep track of the length of an event without having to record the entire event by simply calculating the difference in timestamps.
