# print out a Chrismas Tree :P

# ------*------  1 - spaces = (6 * 2 = 12)
# -----***-----  3 - spaces = (5 * 2 = 10)
# ----*****----  5 - spaces = (4 * 2 = 8)
# ---*******---  7 - spaces = (3 * 2 = 6)
# --*********--  9 - spaces = (2 * 2 = 4)
# -***********- 11 - spaces = (1 * 2 = 2)
# ************* 12 - spaces = (0 * 2 = 0)

def ChristmasTree(height):
    # your code goes here
    stars = 1 
    maxColumns = height * 2 - 1
    for row in range(height):
        spaces = (maxColumns - stars) // 2
        print (spaces * " " + stars * "*" + spaces * " ")
        stars += 2  
              
ChristmasTree(7)
ChristmasTree(11)        
