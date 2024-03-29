from utils import epsilon, vertical_bar, END_ATOM

no = 'Não'
terminal = 'terminal'
entry_atom = 'Átomo de entrada'

class ProductionTable:

    def __init__(self, terminals: "List[str]", non_terminals: "List[str]", productions: "List[Tuple[str, list]]"):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions
        self.first = dict()
        self.second = dict()
        self.table = dict()

    def build_production_table(self, ):
        self.__reset_variables()
        self.get_first()
        self.get_second()
        self.build_table()
        return self.table

    def print_first(self):
        self.print_line(1, 20)
        print(self.get_print_row(['A', 'Primeiro(A)'], 20))
        self.print_line(1, 20)
        for elm in self.first.keys():
            print(self.get_print_row([elm, ' '.join(self.first[elm])], 20))
        self.print_line(1, 20)

    def print_second(self):
        self.print_line(1, 20)
        print(self.get_print_row(['A', 'Seguinte(A)'], 20))
        self.print_line(1, 20)
        for terminal in self.second.keys():
            print(self.get_print_row([terminal, ' '.join(self.second[terminal])], 20))
        self.print_line(1, 20)

    def print_table(self):
        len_of_col = 30
        num_of_col = len(self.terminals + [END_ATOM])

        self.print_table_header(num_of_col, len_of_col)

        for non_terminal in self.non_terminals:

            str_lt_row = []
            for atom in self.terminals + [END_ATOM]:
                key = non_terminal + atom
                if key in self.table:
                    prod = self.table[key]
                    string = self.get_prod_str(prod)
                else:
                    string = ''
                str_lt_row.append(string)

            print_string_row = ''
            print_string_row += ('|{:^%d}|'%len_of_col).format(non_terminal)

            for elm in str_lt_row:
                print_string_row += ('{:^%d}|'%len_of_col).format(elm)

            print(print_string_row)

        self.print_table_footer(num_of_col, len_of_col)

    def print_table_header(self, num_of_col, len_of_col):
        self.print_line(num_of_col, len_of_col)

        string = ''
        string += ('|{:^%d}|'%len_of_col).format('')

        string += ('{:^%d}|'%((len_of_col + 1)*num_of_col - 1)).format(entry_atom)

        print(string)
        self.print_line(num_of_col, len_of_col)

        string = '|'
        print_list = [no + ' ' + terminal] + self.terminals + [END_ATOM]

        for elm in print_list:
            string += ('{:^%d}|' % len_of_col).format(elm)

        print(string)

        self.print_line(num_of_col, len_of_col)

    def print_line(self, num_of_col, len_of_col):
        string = ''
        string += '-' * (len_of_col + 2)
        string += '-' * (num_of_col * (len_of_col + 1))

        print(string)

    def print_table_footer(self, num_of_col, len_of_col):
        self.print_line(num_of_col, len_of_col)

    def get_prod_str(self, prod):
        return prod[0] + " -> " + ''.join(prod[1])

    def build_table(self):
        lt = []
        idx = 0
        for prod in self.productions:
            product = prod[1]
            original_elm = prod[0]
            productions = self.split(product, vertical_bar)
            for production in productions:
                lt.append([])
                lt[idx].append(self.get_prod_str((original_elm, production)))
                alpha = production[0]
                if alpha != epsilon:
                    first_alpha = self.first[alpha]
                else:
                    first_alpha = [epsilon]
                a = original_elm
                first_a = self.first[a]
                second_a = self.second[a]
                for elm_atom in first_alpha:
                    if elm_atom != epsilon:
                        self.table[a + elm_atom] = (a, production)
                    else:
                        for sec_elm_atom in second_a:
                            self.table[a + sec_elm_atom] = (a, production)
                lt[idx].append(first_alpha)
                lt[idx].append(first_a)
                lt[idx].append(second_a)
                idx += 1

        self.print_first_second_table(lt)

    def print_first_second_table(self, lt):
        len_of_col = 30

        self.print_line(3, len_of_col)

        print(self.get_print_row([self.get_prod_str(('A', 'α')), 'Prim(α)', 'Prim(A)', 'Seg(A)'], len_of_col))

        self.print_line(3, len_of_col)

        for row in lt:
            row_lt = []
            for elm in row:
                if type(elm) == type([]):
                    row_lt.append(' '.join(elm))
                else:
                    row_lt.append(elm)
            print(self.get_print_row(row_lt, len_of_col))

        self.print_line(3, len_of_col)

    def get_print_row(self, row, len_of_col):
        string = '|'
        for elm in row:
            string += ('{:^%d}|' % len_of_col).format(elm)
        return string

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

    def split(self, lt: list, elm: any):
        if elm not in lt:
            return [lt]
        for idx in range(len(lt)):
            if lt[idx] == elm:
                return [lt[:idx]] + self.split(lt[idx+1:], elm)
        return [lt]

    def __reset_variables(self):
        self.first = dict()
        self.second = dict()
        self.table = dict()

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
