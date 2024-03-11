Made for COSC3500 Semester 2, 2023

CPU Parallelised Agent-Based Modelling of Infection Spread in C++

Based on real-life infection spread - agent based modelling simulating People that move around in a given World and can be either Susceptible, Infected, or Immune depending on parameters relating to the disease such as infection spread rate, lethality, etc.

Optimised serially through the user of a variety of serial optimisation techniques and analysed performance using GPROF. Optimisations including:
  * Implementing cache friendly code - contiguous memory blocks to store objects
  * Calling conditional statements minimally
  * Reducing the number of method calls when possible
  * Limiting the use of copy propagation
  * Reusing variables to save memory
  * Strength reduction
  * etc

Further implemented into parallel versions, using:
  * OpenMP (1 CPU with multiple threads)
  * MPI and OpenMP (Multiple CPU's with multiple threads)

Implementation of these including the consideration of
  * Communication between threads and nodes
  * Interconnectedness (at the end of each tick in the world, all threads on all nodes needed to communicate at a master node and process information before diverging workload to the different nodes and threads again)

Data was processed and written into a .txt file, which was read and processed in Python to create an animation of the simulation.

![](https://github.com/TrazZed/Parallel-Virus-Spread/blob/main/animation.gif)

Overall performance of each implementation relative to each other:
![image](https://github.com/TrazZed/Parallel-Virus-Spread/assets/125854358/28e5c922-8e8d-46e5-9521-597b1835930b)
