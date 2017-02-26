import math
def fall(theta)

    norm = (90, 200, 20)

    dT = 0.01
    g = -9.8
    l = .125

    dTheta = [0, 0, 0]
    # dThetaEmote = 0
    # dThetaAge = 0
    # dThetaSwag = 0

    ddTheta[0, 0, 0]
    # ddThetaEmote = 0
    # ddThetaAge = 0
    # ddThetaSwag = 0
    thresh
    count = 0
    while count < 200:
        for i, q in enumerate(theta):
            nTheta = q - norm[i]
            nTheta = math.radians(nTheta + dT*dTheta[i])
            dTheta[i] = dTheta[i] + dT*ddTheta[i]
            ddTheta[i] = -g/l*math.sin(math.radians(nTheta))
            theta[i] = math.degrees(nTheta + norm[i])

        count = count+1
