row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]


def place_treasure(position):
    position = position.replace(" ", "")
    if len(position) != 2 or not position.isdigit():
        print("Invalid")
        return
    x = int(position[0])
    y = int(position[1])
    if x < 0 or x > 3:
        print("Invalid")
        return
    elif y < 0 or y > 3:
        print("Invalid")
        return
    
    map[x-1][y-1] = "X"
        
def display():
    for i in map:
        print(i)

def main():
    while True:
        display()
        position = input ("Where do you want to put the treasure ")
        place_treasure(position)
    

if __name__ == "__main__":
    main()