from SearchUtil import *
from utils import * 

romania_map = UndirectedGraph(dict(
    A=dict(Z=75, S=140, T=118),
    B=dict(U=85, P=101, G=90, F=211),
    C=dict(D=120, R=146, P=138),
    D=dict(M=75),
    E=dict(H=86),
    F=dict(S=99),
    H=dict(U=98),
    I=dict(V=92, N=87),
    L=dict(T=111, M=70),
    O=dict(Z=71, S=151),
    P=dict(R=97),
    R=dict(S=80),
    U=dict(V=142)))
romania_map.locations = dict(
    A=(91, 492), B=(400, 327), C=(253, 288),
    D=(165, 299), E=(562, 293), F=(305, 449),
    G=(375, 270), H=(534, 350), I=(473, 506),
    L=(165, 379), M=(168, 339), N=(406, 537),
    O=(131, 571), P=(320, 368), R=(233, 410),
    S=(207, 457), T=(94, 410), U=(456, 350),
    V=(509, 444), Z=(108, 531))
romania_problem = GraphProblem('A', 'B', romania_map)
straight_line_to_bucharest_slides = dict(
    A = 366,
    B = 0,
    C = 160, 
    D = 242, 
    E = 161,
    F = 178,
    G = 77, 
    H = 151, 
    I = 226,
    L = 244, 
    M = 241, 
    N = 234,
    O = 380,
    P = 98,
    R = 193,
    S = 253,
    T = 329,
    U = 80,
    V = 199,
    Z = 374
)
straight_line_to_bucharest_slides_repository = {str(k) : int(distance(romania_map.locations[str(k)], romania_map.locations["B"])) for k in romania_map.locations.keys()}

#https://www.eurail.com/en/plan-your-trip/trip-ideas/top-destinations/switzerland-train#tabs-164391249f-item-06ee39b43c-tab
# Durations (in Minutes) taken from quickest train durations found on SBB website on a random day
switzerland_map = UndirectedGraph(dict(
    Geneva=dict(Lausanne=35),
    Lausanne=dict(Neuchátel=41, Bern=67, Visp=92),
    Neuchátel=dict(Basel = 90),
    Basel=dict(Olten=25),
    Olten=dict(Zürich=30, Lucerne = 35, Bern = 45),
    Bern=dict(Interlaken=52),
    Zürich=dict(Chur=74, Lugano = 113),
    Lucerne=dict(Zürich=41, Lugano=100, Chur = 128),
    Interlaken=dict(Lucerne=108),
    Visp=dict(Bern=57, Interlaken=52),
    Zermatt=dict(Visp=66),
    Chur=dict(),
    Lugano=dict(Chur=155)))
straight_line_to_lucerne = dict(
    Geneva = 366,
    Lausanne = 389,
    Neuchátel = 160, 
    Basel = 242, 
    Olten = 161,
    Bern = 178,
    Zürich = 77, 
    Lucerne = 0, 
    Interlaken = 226,
    Visp = 244, 
    Zermatt = 241, 
    Chur = 234,
    Lugano = 380
)
switzerland_problem = GraphProblem('Geneva', 'Lucerne', switzerland_map)

ex2a1 = Graph(dict(
    A=dict(B=1, C =3, D=5),
    B=dict(C=1, E=3),
    C=dict(D = 1),
    D=dict(F=1),
    E=dict(A=2),
    F=dict(C=2),
    ))
ex2a1_problem = GraphProblem('A', 'F', ex2a1)

ex2b1 = UndirectedGraph(dict(
    A=dict(B=5, C =10),
    B=dict(C=1, D=20),
    C = dict(D = 10),
    D = dict()
    ))
ex2b1_heuristic = dict(
    A = 5,
    B = 10,
    C = 1,
    D = 0
)
ex2b1_problem = GraphProblem('A', 'D', ex2b1)