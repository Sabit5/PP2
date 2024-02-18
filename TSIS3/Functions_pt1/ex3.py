def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        if 2*numchickens + 4*numrabbits == numlegs:
            return numchickens, numrabbits
    return "No solution"


if __name__ == "__main__":
    numheads = int(input("Enter the number of heads: "))
    numlegs = int(input("Enter the number of legs: "))

    result = solve(numheads, numlegs)
    if result != "No solution":
        numchickens, numrabbits = result
        print("Number of chickens:", numchickens)
        print("Number of rabbits:", numrabbits)
    else:
        print("No solution found.")