def move(rings, src, dest, aux):
    global count
    if rings == 1:
        print(f"Move {src} to {dest}")
        count = count + 1
    else:
        move(rings-1, src, aux, dest)
        print(f"Move {src} to {dest}")
        move(rings-1, aux, dest, src)
        count = count + 1


n = int(input(print("Enter no. of rings: ")))
count = 0
move(n, 'A', 'B', 'C')
print("Total Moves = ", count)
