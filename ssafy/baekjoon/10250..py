def solve(floors, rooms, guest):
    floor = guest % floors if guest % floors else floors
    room = 1
    while guest > floors:
        guest -= floors
        room += 1
    room = str(room)
    num = str(floor) + (room if len(room) >= 2 else '0' + room)
    return num


T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    print(solve(h, w, n))
