# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Pro of this method is that the storage will be evenly used so no server will be overloaded while others are not being used as much. Con of this method is that query needs to be run on all 3 servers so it takes more query power and time to consolidate the observations.

## Partitioning by Hour

Pro of this method is the usage and load is more predictable based on patterns, so if there's a need in increasing capacities to accomodate more popular boat (such as boat A) then the upgrade is more precise. However with this uneven distribution of data, boat B will stay amost idle whereas A is being stored and queried frequently.

## Partitioning by Hash Value

The advantage of using Hash Value are: firstly the usage is evenly distributed since it's distributing in an order amongst 3 boats, so all boats are used equally; secondly hash value works as a reference to the location of the server which helps with identifying the exact boat if the hash reference is known; con is that if a user doesn't know the relationship between certain timestamp and hash value (almost like an additional dictionary), then they still need to query all 3 boats to find out.