from utils import epsilon, vertical_bar


class ProductionTable:

    def __init__(self, terminals: List[str], non_terminals: List[str], productions: List[Tuple[str, list]]):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions
        self.first = dict()

    def build_production_table(self, ):
        self.__reset_variables()
        self.get_first()

    def get_first(self):
        self.initialize_fist()
        self.rotary_convergent_process()
        return self.first

    def initialize_fist(self):
        for terminal in self.terminals:
            self.first[terminal] = [terminal]

        for prod in self.productions:
            if epsilon in prod[1]:
                self.first[prod[0]] = [epsilon]

    def rotary_convergent_process(self):
        while True:
            initial_first = self.copy_first()
            for prod in self.productions:
                if prod[1]:
                    if prod[1][0] != epsilon and prod[1][0] != vertical_bar:
                        for elm in self.first[prod[1][0]]:
                            if elm not in self.first[prod[0]]:
                                self.first[prod[0]].append(elm)
            if self.equals(initial_first, self.first):
                break

    def __reset_variables(self):
        self.first = dict()

    def copy_first(self):
        first_copy = dict()
        for key in self.first.keys():
            lt = self.first[key]
            first_copy[key] = lt.copy()
        return first_copy

    def equals(self, initial_first, first):
        for key in first.keys():
            lt_1 = first[key]
            lt_2 = initial_first[key]
            if lt_1 != lt_2:
                return False
        return True
