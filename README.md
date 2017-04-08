# Monte_Carlo_Simulations

Monte Carlo simulations work by using random numbers. You define a problem region and run the simulation until it converges to an answer. As with any random number system, there is inherent uncertainty, but after thousands of steps, it's likely you'll get within a few sigfigs of the right answer.

One example of a Monte Carlo simulation is shown in this repository (approximating_pi.py). This code works by generating random points in the x-y plane.

The points are generated inside a square. Inside that square is a circle, when each point is generated, if the distance to the origin is less than or equal to the circle radius, it is said to be "inside" the circle.

After many points are simulated, the program divides the inner point count by the outer point count and multiplies by 4. This is because the area equations are (given that h = square side length):

a(rect) = h^2 and a(circle) = 0.25\*pi\*h^2

Divide inner by outer and you get pi/4. Because of the nature of random numbers, this simulation will not "find" pi so much as converge to pi. The values are stored and graphed to demonstrate this concept.
