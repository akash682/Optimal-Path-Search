import heapq as Q
import sys

# g(n)
f_name = sys.argv[2]
ax = open(f_name, "r")
data1 = ax.read()
data1 = data1.split()
sz_data1 = len(data1)
DATA1 = []

for i in range(0, sz_data1 - 3):
    a = i % 3
    if a == 0:
        DATA1.append([data1[i], data1[i + 1], data1[i + 2]])
        continue
    else:
        continue

for i in range(0, sz_data1 - 3):
    a = i % 3
    if a == 0:
        DATA1.append([data1[i + 1], data1[i], data1[i + 2]])
        continue
    else:
        continue

# h(n)
f_name = sys.argv[5]
ax = open(f_name, "r")
data1 = ax.read()
data1 = data1.split()
sz_data1 = len(data1)
HEUR = []

for i in range(0, sz_data1 - 1):
    a = i % 2
    if a == 0:
        HEUR.append([data1[i], data1[i + 1]])
        continue
    else:
        continue

origin = sys.argv[3]
current = origin
destination = sys.argv[4]

#UNIMFORMED SEARCH
if sys.argv[1] == 'uninf':

    sz_gn = len(DATA1)
    queue = []
    Q.heappush(queue, (0, [origin], 0))

    while not queue == []:
        WAY = Q.heappop(queue)
        current = WAY[1][len(WAY[1]) - 1]

        if destination in WAY[1]:
            print("distance: " + str(WAY[2]) + "km")
            sz_WAY = len(WAY[1])
            for i in range(0, sz_WAY-1):
                for a in range(0, sz_gn-1):
                    if DATA1[a][0] == WAY[1][i]:
                        if DATA1[a][1] == WAY[1][i+1]:
                            dist = DATA1[a][2]
                print(str(WAY[1][i]) + " to " + str(WAY[1][i+1]) + ", " + dist + "km")
            break

        for i in range(0, sz_gn - 1):
            SEARCH = DATA1[i][0]
            if SEARCH == current:
                Michi = WAY[1][:]
                cost = WAY[0]
                dist = WAY[2]
                PATH = DATA1[i][:]
                Michi.append(PATH[1])
                Q.heappush(queue, (cost + int(PATH[2]), Michi, dist+int(PATH[2])))
                Michi = []
                continue
            else:
                continue

# INFORMED SEARCH
if sys.argv[1] == 'inf':

    sz_gn = len(DATA1)
    sz_hn = len(HEUR)

    queue = []
    Q.heappush(queue, (0, [origin], 0))

    while not queue == []:
        WAY = Q.heappop(queue)
        current = WAY[1][len(WAY[1]) - 1]

        if destination in WAY[1]:
            print("distance: " + str(WAY[2]) + "km")
            sz_WAY = len(WAY[1])
            for i in range(0, sz_WAY-1):
                for a in range(0,sz_gn-1):
                    if DATA1[a][0] == WAY[1][i]:
                        if DATA1[a][1] == WAY[1][i+1]:
                            dist = DATA1[a][2]
                print(str(WAY[1][i]) + " to " + str(WAY[1][i+1]) + ", " + dist + "km")
            break

        for i in range(0, sz_gn - 1):
            SEARCH = DATA1[i][0]
            if SEARCH == current:
                Michi = WAY[1][:]
                cost = WAY[0]
                dist = WAY[2]
                for j in range(0, sz_hn - 1):
                    DEST = HEUR[j][0]
                    if DEST == Michi[-1]:
                        hr = HEUR[j][1]
                        break

                PATH = DATA1[i][:]
                Michi.append(PATH[1])
                Q.heappush(queue,(cost + int(PATH[2]) + int(hr), Michi, dist+int(PATH[2])))
                Michi = []
                continue
            else:
                continue