import matplotlib.pyplot as plt

from bezier import *
from bspline import *



liste_test_exemple_cours_bezier = [(0, 0), (16, 16), (32, 16), (48, 0)]
liste_test_exemple_cours_bspline = [(0, 0), (0, 24), (24, 24), (24, 0), (0, 0), (0, 24)]
liste_test_alpha = [(-20, 0), (0, 0), (20, 0), (20, 20), (0, 20), (0, -20), (-10, -10)]
liste_test_5 = [(8, 24), (2, 0), (4, -8), (5, -8), (6, -8), (8, 0), (0, 24), (-8, -8), (0, -24), (16, -16),
                (32, 0), (32, 16), (16, 32), (0, 32), (0, 64), (32, 64)]

'''plt.figure(1)
testFormeControle(liste_test_exemple_cours_bezier)
plt.figure(2)
plt.title("Bezier")
tracerCourbesBezier(liste_test_exemple_cours_bezier,0.01)'''



plt.figure(1)
plt.title("BSPLINE uniforme")
tracerCourbeBspline(liste_test_5, 0.1, 3, type_vecteur="u")
plt.figure(2)
plt.title("BSPLINE ouvert uniforme")
tracerCourbeBspline(liste_test_5, 0.1, 3, type_vecteur="ou")
plt.figure(3)
plt.title("BSPLINE quelquonque")
tracerCourbeBspline(liste_test_5, 0.1, 3, type_vecteur="q")
plt.figure(4)
plt.title("Bezier")
tracerCourbesBezier(liste_test_5,0.1)
plt.figure(5)
plt.title("Bezier par morceaux (cubique)")
tracerCourbesBezier(liste_test_5,0.1,True)

