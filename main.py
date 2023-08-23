# Input the thickness of the pattern
thickness = int(input())

# Character for the pattern
c = 'H'

# Top Cone
# Prints the top cone of the pattern
for i in range(thickness):
    # Prints left-padded and right-padded characters to form a cone
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
# Prints the top pillars of the pattern
for i in range(thickness+1):
    # Prints centered characters to create the top pillars
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
# Prints the middle belt of the pattern
for i in range((thickness+1)//2):
    # Prints centered characters to form the middle belt
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
# Prints the bottom pillars of the pattern
for i in range(thickness+1):
    # Prints centered characters to create the bottom pillars
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
# Prints the bottom cone of the pattern
for i in range(thickness):
    # Prints right-padded, left-padded, and right-justified characters to form a cone
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
