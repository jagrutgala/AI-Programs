"""
p7_tower_of_hanoi.py
Author: Jagrut Gala
Date: 04-09-2021
Practical: 7
Objective: Demonstrate Tower of Hanoi Problem.
"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod): # f:A t:C x:B
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
    
# Driver code
n = 4 # n is number of disks
# A B C are rods
print(f"Jagrut Tower of Hanoi")
TowerOfHanoi(n, 'A', 'C', 'B')
