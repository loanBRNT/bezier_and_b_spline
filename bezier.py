import matplotlib.pyplot as plt
import numpy as np


def trianglePascal(n: int):
    '''
    Calcul des coéfficients binomiaux pour n
    :param n: ordre du triangle de pascal
    :return: liste des coef binomiaux correspondant à n
    '''
    P = np.zeros((n, n))
    P[0, 0] = 1
    P[1, 0] = 1
    P[1, 1] = 1
    for i in range(2, n):
        for j in range(0, i + 1):
            P[i, j] = P[i - 1, j - 1] + P[i - 1, j]
    return P[n - 1]


def courbesBezier(u: float, pts_controle):
    n = len(pts_controle) - 1
    coefBinomiaux = trianglePascal(n + 1)
    p = (0, 0)
    for i in range(n + 1):
        Ci = int(coefBinomiaux[i])
        Bi = Ci * (u ** i) * ((1 - u) ** (n - i))
        p = (p[0] + pts_controle[i][0] * Bi, p[1] + pts_controle[i][1] * Bi)
    return p


def miniBezier(pas, pts_controle):
    x_bez = []
    y_bez = []
    u = 0.0
    while u < 1.0:
        p = courbesBezier(u, pts_controle)
        x_bez.append(p[0])
        y_bez.append(p[1])
        u += pas
    return x_bez, y_bez


def tracerCourbesBezier(pts_controle,pas: float, decoupage_cubique=False, intervalle=3):
    '''
    Trace une courbe de Bézier
    :param pts_controle: liste des points de contrôles
    :param pas: pas de traçage
    :param decoupage_cubique: Si True, on trace une Bézier par morceaux
    :param intervalle: Intervalle à prendre pour les morceaux (3 = cubique)
    :return:
    '''
    x_ctrl = []
    y_ctrl = []

    if not decoupage_cubique:
        # Tracer traditionnel
        x_bez, y_bez = miniBezier(pas, pts_controle)
    else:
        x_bez = []
        y_bez = []
        # Tracer par morceaux
        for i in range(0, len(pts_controle), intervalle):
            if i < len(pts_controle)-3:
                pts_guez = pts_controle[i:i + 4]
                x_guez, y_guez = miniBezier(pas, pts_guez)
                x_bez = x_bez + x_guez
                y_bez = y_bez + y_guez
            else:
                if i+1 < len(pts_controle):
                    x_guez = [pts_controle[i][0]]
                    y_guez = [pts_controle[i][0]]
                    x_guez.append(pts_controle[i+1][0])
                    y_guez.append(pts_controle[i+1][0])
                    if i+2 < len(pts_controle):
                        x_guez.append(pts_controle[i+2][0])
                        y_guez.append(pts_controle[i+2][0])
                    x_bez = x_bez + x_guez
                    y_bez = y_bez + y_guez


    for pts in pts_controle:
        x_ctrl.append(pts[0])
        y_ctrl.append(pts[1])


    plt.plot(x_ctrl, y_ctrl,'g--')
    plt.plot(x_bez, y_bez,'b')
    plt.plot(x_ctrl, y_ctrl, 'rx')
    plt.show()


def testFormeControle(pts_controle):
    '''
    Permet d'afficher la forme des points de contrôles (pour debugger)
    :param pts_controle: liste des points de contrôles
    '''
    x_ctrl = []
    y_ctrl = []

    for pts in pts_controle:
        x_ctrl.append(pts[0])
        y_ctrl.append(pts[1])


    plt.plot(x_ctrl, y_ctrl,'g--')
    plt.plot(x_ctrl, y_ctrl,'ro')
    plt.show()
