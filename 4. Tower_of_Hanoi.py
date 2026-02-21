def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solves the Towers of Hanoi problem recursively.
    
    Parameters:
    n (int): The number of disks.
    source (str): The name of the starting peg.
    destination (str): The name of the target peg.
    auxiliary (str): The name of the helper peg.
    """
    # Base case: If there's only one disk, just move it to the destination
    if n == 1:
        print(f"Move disk 1 from peg {source} to peg {destination}")
        return
    
    # Step 1: Move the top n-1 disks from source to auxiliary peg
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth disk (the largest one) from source to destination peg
    print(f"Move disk {n} from peg {source} to peg {destination}")
    
    # Step 3: Move the n-1 disks from the auxiliary peg to the destination peg
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# --- Example Usage ---
if _name_ == "_main_":
    number_of_disks = 3
    print(f"Solving Towers of Hanoi for {number_of_disks} disks:\n")
    
    # A is the starting peg, C is the target peg, B is the helper peg
    tower_of_hanoi(number_of_disks, 'A', 'C', 'B')
