from AlgResults import *
from searchExamples import * 
from GraphUtil import * 
import argparse

parser = argparse.ArgumentParser(description='Practice search algorithms')

group = parser.add_mutually_exclusive_group()
group.add_argument('-ro', action='store_true', help='Use the romania map')
group.add_argument('-ch', action='store_true', help='Use the switzerland map')
group.add_argument('-r', action='store_true', help='Generate a random graph with specified num of nodes, seed and prob')

parser.add_argument('--n', metavar='Nodes', type = int, default= 10, help='Specify how many nodes should be created in a random graph')
parser.add_argument('--s', metavar='Seed', type = int, default= None, help='Specify what seed should be used in the creation of the random graph')
parser.add_argument('--p', metavar='Probability', type = float, default= 0.065, help='Specify what probability nodes should be connected with in a random graph (Not quite, since the graph is guaranteed to be connected)')
args = parser.parse_args()

if args.ro:
    p, h = switzerland_problem, straight_line_to_lucerne
    name = "romania"
    generate_graph_svg(p, h, name, override=False, font_color="orange")
elif args.ch:
    p, h = switzerland_problem, straight_line_to_lucerne
    name = "ch"
    generate_graph_svg(p, h, name, override=False, font_color="orange")
elif args.r:
    nodes, seed, prob = args.n, args.s, args.p
    p, h, seed = random_problem(nodes = nodes, seed=seed, p = prob)
    name = str(seed)+"_"+str(nodes)+"_"+str(prob)
    generate_graph_svg(p, h, name, override=False, font_color="orange")
else:
    parser.print_help()

cont = True 
while cont:
    cont = input("Want to regenerate " + name + ".svg?: [n/Anything else]\n").lower() != 'n'
    if(cont):
        generate_graph_svg(p, h, name, override=True, font_color="orange")
    else:
        break

res = expansion_order(p, lambda n: h[n.state], steps=5)

keys = set(list(res.keys()))
for k in keys: 
    print(k+":")
    print("".format(input("")))
    print("-".join([n.state for n in res[k]]))
    print("".format(input("")))