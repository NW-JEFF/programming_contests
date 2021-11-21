"""Wrong; [130, -130, 30, -180]; didn't consider on -180."""

n = int(input())
x0, y0 = map(int, input().split())  # starting point, in fact independent of latitude
now = y0
inter1 = [now, now]  # range of longitude visited, including current location
inter2 = None  # range of longitude visited, not including current location

pass_pole = False

for _ in range(n-1):
    x,y = map(int, input().split())
    if pass_pole:  # once visited the pole, already 'yes'
        continue

    elif abs(y - now) == 180:  # pass the north or south pole
        pass_pole = True
        continue

    else:
        if abs(y - now) < 180:  # minor arc does not pass negative axis
            if y - now > 0:  # counter-clockwise
                if y > inter1[1]:  # update right end
                    inter1[1] = y
            elif y - now < 0:  # clockwise
                if y < inter1[0]:
                    inter1[0] = y
            # ignore == 0 
            now = y  # update position
        else:  # pass negative axis
            if y - now > 0:  # clockwise
                if not inter2:
                    inter2 = [y,180]
                    inter1 = [-180,inter1[1]]
                    inter1, inter2 = inter2, inter1  # make inter1 contain new position
                else:
                    if y < inter2[0]:
                        inter2 = [y,180]
                    inter1, inter2 = inter2, inter1

            elif y - now < 0:  # counter-clockwise
                if not inter2:
                    inter2 = [-180,y]
                    inter1 = [inter1[0],180]
                    inter1, inter2 = inter2, inter1  # make inter1 contain new position
                else:
                    if y > inter2[1]:
                        inter2 = [-180,y]
                    inter1, inter2 = inter2, inter1
            now = y

y = y0  # finally come back toy0
if pass_pole:  # once visited the pole, already 'yes'
    pass

elif abs(y - now) == 180:  # pass the north or south pole
    pass_pole = True

else:
    if abs(y - now) < 180:  # minor arc does not pass negative axis
        if y - now > 0:  # counter-clockwise
            if y > inter1[1]:  # update right end
                inter1[1] = y
        elif y - now < 0:  # clockwise
            if y < inter1[0]:
                inter1[0] = y
    else:  # pass negative axis
        if y - now > 0:  # clockwise
            if not inter2:
                inter2 = [y,180]
                inter1 = [-180,inter1[1]]
            else:
                if y < inter2[0]:
                    inter2 = [y,180]

        elif y - now < 0:  # counter-clockwise
            if not inter2:
                inter2 = [-180,y]
                inter1 = [inter1[0],180]
            else:
                if y > inter2[1]:
                    inter2 = [-180,y]

if pass_pole:
    print('yes')
else:
    if not inter2:
        a = inter1[0]+180
        b = 180-inter1[1]
        if a==0 and b==0:
            print('yes')
        elif a>0:
            print('no', inter1[0]-0.5)
        else:
            print('no', inter1[1]+0.5)
    else:
        if inter1[0] == -180:
            if inter1[1] >= inter2[0]:
                print('yes')
            else:
                print('no', inter1[1]+0.5)
        else:  # inter1[1] == 180
            if inter1[0] <= inter2[1]:
                print('yes')
            else:
                print('no', inter1[0]-0.5)

    # print(inter1, inter2)
