#Exercise 1: Compute time of collision with distance and speed using a lambda function
speed = int(input('Enter the speed (km/h): '))
distance = int(input('Enter the distance between the vehicles (meters): '))
collisionTime = lambda distance, speed: (distance / (speed * 1000) * 3600)
print(f'The collision will occur in {collisionTime(distance, speed)} seconds')