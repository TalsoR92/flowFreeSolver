L1 = [1, 2, 3, 4, 5]

L2 = [L1 for i in range(1, 2)]

import time

# a = time.time()
# for i in range(10000000):
#     # liste_nombres.append(2)
#     # liste_de_listes.append(liste_nombres)
#     # liste_nombres.append(2)
#     liste_de_listes.append((liste_nombres + [2]))

# print(time.time()-a)

L2.append((L1))
print(L2)

L1.append(9)
print(L2)