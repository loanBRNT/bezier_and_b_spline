import matplotlib.pyplot as plt
import numpy as np
import random as rd


def floraison(u, U, k, pts_controle):
    '''

    :param u: u à calculer
    :param U: vecteur nodal
    :param k: ordre
    :param pts_controle: liste des pts de controles
    :return: P(u)
    '''
    dec = 0
    while u > U[dec + k]:
        dec += 1
    PTS = pts_controle[dec:dec + k]
    for j in range(k - 1):
        for i in range(k - j - 1):
            coef1 = ((U[dec + k + i] - u) / (U[dec + k + i] - U[dec + i + 1 + j]))
            coef2 = ((u - U[dec + 1 + i + j]) / (U[dec + k + i] - U[dec + i + 1 + j]))
            x = coef1 * PTS[i][0] + coef2 * PTS[i + 1][0]
            y = coef1 * PTS[i][1] + coef2 * PTS[i + 1][1]
            PTS[i] = (x, y)

    return PTS[0]


def tracerCourbeBspline(pts_controle, pas, ordre,type_vecteur="u",val_deb=0,pas_nodal=1):
    '''
    Trace une B-SPLINE
    :param pts_controle: liste des points de contrôle
    :param pas: le pas de traçage
    :param ordre: ordre de la B-SPLINE
    :param type_vecteur: "u" -> uniforme, "ou" -> ouvert uniforme, "q" -> quelquonque
    :param val_deb: valeur de départ du vecteur nodal
    :param pas_nodal: pas au sein du vecteur nodal
    :return: x,y listes des coordonnees de la B-SPLINE
    '''
    x = []
    y = []
    x_c = []
    y_c = []
    for p in pts_controle:
        x_c.append(p[0])
        y_c.append(p[1])
    n = len(pts_controle)
    if type_vecteur == "u":
        U = np.arange(val_deb, pas_nodal*(val_deb + n + ordre), pas_nodal)
    elif type_vecteur == "ou":
        U1 = [val_deb for e in range(ordre)]
        U = [val_deb+(i*pas_nodal) for i in range(1,val_deb + n + ordre - 1 - (ordre-1)*2)]
        U2 = [val_deb + n + ordre - 1 - (ordre-1)*2 for e in range(ordre)]

        U = np.array(U1 + U + U2)
    elif type_vecteur == "q":
        U = [val_deb]
        for e in range(n + ordre-1):
            U.append(rd.randint(U[e]+1,U[e]*2+1))
    else:
        print("ERREUR :",type_vecteur," inconnue (utilisez 'u' pour uniforme, "
                                      "'ou' pour ouvert uniforme, 'q' pour quelquonque")
        exit(-1)


    u = U[ordre-1]
    while u < float(U[n]):
        p = floraison(u, U, ordre, pts_controle)
        x.append(p[0])
        y.append(p[1])
        u += pas

    plt.plot(x, y,"b")
    plt.plot(x_c,y_c,"g--")
    plt.plot(x_c, y_c, "r+")
    plt.show()

    return x, y
