from utils import epsilon, vertical_bar, END_ATOM


class ProductionTable:

    def __init__(self, terminals: "List[str]", non_terminals: "List[str]", productions: "List[Tuple[str, list]]"):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions
        self.first = dict()
        self.second = dict()

    def build_production_table(self, ):
        self.__reset_variables()
        self.get_first()
        self.get_second()

    def get_second(self):
        if not self.first: raise Exception('You need to call get_fist before call get_second')
        self.trivial_initialization_second()
        self.non_trivial_initialization_second()
        self.rotary_convergent_process_second()
        return self.second

    def trivial_initialization_second(self):
        if not self.non_terminals: raise Exception('Non terminals empty')
        initial_symbol = self.non_terminals[0]
        self.second[initial_symbol] = [END_ATOM]
        for non_terminal in self.non_terminals:
            if non_terminal != initial_symbol:
                self.second[non_terminal] = []

    def non_trivial_initialization_second(self):
        for prod in self.productions:
            product = prod[1]
            products = self.split(product, vertical_bar)
            for product in products:
                for idx in range(len(product) - 1):
                    elm = product[idx]
                    if elm in self.non_terminals:
                        # insert in second:
                        next_elm = product[idx + 1]
                        for first in self.first[next_elm]:
                            if first != epsilon and first not in self.second[elm]:
                                self.second[elm].append(first)

    def rotary_convergent_process_second(self):
        while True:
            initial_second = self.copy_first_or_second(self.second)
            for prod in self.productions:
                origin_elm = prod[0]
                product = prod[1]
                products = self.split(product, vertical_bar)
                for product in products:
                    last_elm = product[-1]
                    if last_elm != epsilon:
                        if epsilon in self.first[last_elm]:
                            for elm in product:
                                if elm in self.non_terminals:
                                    for next in self.second[origin_elm]:
                                        if next not in self.second[elm]:
                                            self.second[elm].append(next)
            if self.equals(initial_second, self.second):
                break

    def get_first(self):
        self.initialize_fist()
        self.rotary_convergent_process_first()
        return self.first

    def initialize_fist(self):
        for terminal in self.terminals:
            self.first[terminal] = [terminal]

        for prod in self.productions:
            if epsilon in prod[1]:
                self.first[prod[0]] = [epsilon]
            else:
                self.first[prod[0]] = []

    def rotary_convergent_process_first(self):
        while True:
            initial_first = self.copy_first_or_second(self.first)
            for prod in self.productions:
                if prod[1]:
                    sub_prods = self.split(prod[1], vertical_bar)
                    for sub_prod in sub_prods:
                        if sub_prod:
                            if sub_prod[0] != epsilon:
                                for elm in self.first[sub_prod[0]]:
                                    if elm not in self.first[prod[0]]:
                                        self.first[prod[0]].append(elm)
            if self.equals(initial_first, self.first):
                break

    def split(self, lt: list, elm: any, rec=False):
        if elm not in lt:
            if rec: return lt
            else: return [lt]
        for idx in range(len(lt)):
            if lt[idx] == elm:
                return [lt[:idx]] + [self.split(lt[idx+1:], elm, rec=True)]
        return [lt]

    def __reset_variables(self):
        self.first = dict()
        self.second = dict()

    def copy_first_or_second(self, dictionary):
        copy = dict()
        for key in dictionary.keys():
            lt = dictionary[key]
            copy[key] = lt.copy()
        return copy

    def equals(self, initial_first, first):
        for key in first.keys():
            lt_1 = first[key]
            lt_2 = initial_first[key]
            if lt_1 != lt_2:
                return False
        return True
