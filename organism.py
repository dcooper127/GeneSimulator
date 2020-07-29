# Object used to represent an organism.
# Contains two alleles to represent its genotype, each of which are either dominant or reccesive

class organism:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2