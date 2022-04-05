map = [
        [12, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],    
        [0, 0, 0, 0, 24]
]

VABA_TEE = 0
SEIN = 1

start_x = 0
start_y = 0

def saab_liikuda_paremale(map, praegused_kordinaadid):
    print("SIIN TOIMUB SEE")
    print(praegused_kordinaadid)
    print(map[0][1] == VABA_TEE)
    print("SIIN TOIMUB SEE")
    return False

print(saab_liikuda_paremale(map, [start_x, start_y]))
print(saab_liikuda_paremale(map, [1, 1]))

def print_kaart():
    print(map[0])
    print(map[1])
    print(map[2])
    print(map[3])
    print(map[4])

print_kaart()