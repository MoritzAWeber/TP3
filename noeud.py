import math, operator

class Noeud:

    def __init__(self, val, enfants):
        self.val = val
        self.enfants = enfants

    def ajouteNoeud(self, noeud):
        self.enfants = self.enfants.append(noeud)

    def affichagePolonais(self):
        print(self.val, end=" ")
        for enfant in self.enfants:
            enfant.affichagePolonais()

    def evaluer(self, values):
        OPS = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "exp": math.exp,
            "log": math.log,
            "sin": math.sin,
            "cos": math.cos,
        }
        if self.val in OPS:
            resultEnfants = [enfant.evaluer(values) for enfant in self.enfants]
            return OPS[self.val](*resultEnfants)
        
        elif self.val in values:
            return values[self.val]
        
        else:
            try:
                return float(self.val)
            except:
                raise ValueError(f"Valeur inconnue: {self.val}")
