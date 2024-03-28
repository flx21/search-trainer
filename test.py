from AlgResults import *
from searchExamples import * 

res = expansion_order(switzerland_problem, lambda n: straight_line_to_lucerne[n.state], 10)
for n, e in res.items():
    print(n+":\n", " - ".join([n.state for n in e]), "\n")