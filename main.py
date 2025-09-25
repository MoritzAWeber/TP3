import utils
import graph
import noeud as nd

expression = nd.Noeud("exp", [nd.Noeud("+", [nd.Noeud(2, []), nd.Noeud("y", [])])])
expression.affichagePolonais()
expression.evaluer({"y": -2})