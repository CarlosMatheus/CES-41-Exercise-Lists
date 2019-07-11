END_ATOM = '$'
Expand_action = 'Expandir'
unstack_action = 'Dempilhar, avançar'
epsilon = 'ε'


class Analyser:
    def __init__(self):
        self.end_atom = END_ATOM
        self.atoms = ['id', '+', '*', '(', ')', self.end_atom]
        self.non_terminals = ['E', "E'", 'T', "T'", 'F']
        self.stack = Stack()

        self.entry = [self.end_atom]
        self.actual_char = self.end_atom
        self.actual_char_idx = 0

        self.table = self.__create_table()

    def analyse(self, entry):
        if not self.non_terminals: raise Exception('non terminals are empty')
        if not self.entry: raise Exception('empty entry')

        self.__reset_entry(entry)

        self.stack.push(self.end_atom)
        self.stack.push(self.non_terminals[0])

        while self.stack:
            actual_production = self.stack.top()
            actual_char = self.__get_actual_char()
            initial_stack = self.stack.copy()
            initial_entry = self.__get_entry_state()

            if self.__is_non_terminal(actual_production):
                self.stack.pop()

                actual_actions = Expand_action

                next_productions = self.table[actual_production + actual_char]

                if next_productions is None:
                    print("Compilation Error")
                    return

                for production in next_productions[::-1]:
                    self.stack.push(production)
            else:
                actual_actions = unstack_action
                next_productions = None
                self.__next_char()
                self.stack.pop()

            self.__print_current_action(initial_stack, initial_entry, actual_actions, actual_production, next_productions)

    def __get_entry_state(self):
        return self.entry[self.actual_char_idx:]

    def __is_non_terminal(self, prod):
        return prod in self.non_terminals

    def __set_entry(self, entry):
        self.entry = entry

    def __get_actual_char(self):
        return self.entry[self.actual_char_idx]

    def __next_char(self):
        self.actual_char_idx += 1
        return self.entry[self.actual_char_idx]

    def __reset_entry(self, entry=[END_ATOM]):
        self.entry = entry
        self.actual_char = self.entry[0]
        self.actual_char_idx = 0

    def __create_table(self):
        self.table = dict()
        self.table[self.non_terminals[0] + self.atoms[0]] = ['T', "E'"]
        self.table[self.non_terminals[1] + self.atoms[0]] = []
        self.table[self.non_terminals[2] + self.atoms[0]] = ['F', "T'"]
        self.table[self.non_terminals[3] + self.atoms[0]] = []
        self.table[self.non_terminals[4] + self.atoms[0]] = ['id']

        self.table[self.non_terminals[0] + self.atoms[1]] = []
        self.table[self.non_terminals[1] + self.atoms[1]] = ['T', "E'"]
        self.table[self.non_terminals[2] + self.atoms[1]] = []
        self.table[self.non_terminals[3] + self.atoms[1]] = [epsilon]
        self.table[self.non_terminals[4] + self.atoms[1]] = []

        self.table[self.non_terminals[0] + self.atoms[2]] = []
        self.table[self.non_terminals[1] + self.atoms[2]] = []
        self.table[self.non_terminals[2] + self.atoms[2]] = []
        self.table[self.non_terminals[3] + self.atoms[2]] = ['*', 'F', "T'"]
        self.table[self.non_terminals[4] + self.atoms[2]] = []

        self.table[self.non_terminals[0] + self.atoms[3]] = ['T', "E'"]
        self.table[self.non_terminals[1] + self.atoms[3]] = []
        self.table[self.non_terminals[2] + self.atoms[3]] = ['F', "T'"]
        self.table[self.non_terminals[3] + self.atoms[3]] = []
        self.table[self.non_terminals[4] + self.atoms[3]] = ['(', 'E', ')']

        self.table[self.non_terminals[0] + self.atoms[4]] = []
        self.table[self.non_terminals[1] + self.atoms[4]] = [epsilon]
        self.table[self.non_terminals[2] + self.atoms[4]] = []
        self.table[self.non_terminals[3] + self.atoms[4]] = [epsilon]
        self.table[self.non_terminals[4] + self.atoms[4]] = []

        self.table[self.non_terminals[0] + self.atoms[5]] = []
        self.table[self.non_terminals[1] + self.atoms[5]] = [epsilon]
        self.table[self.non_terminals[2] + self.atoms[5]] = []
        self.table[self.non_terminals[3] + self.atoms[5]] = [epsilon]
        self.table[self.non_terminals[4] + self.atoms[5]] = []

        return self.table

    def __print_current_action(self, stack, entry, action, production, next_productions):
        if next_productions is not None:
            prod = production + ' -> ' + ''.join(next_productions)
        else:
            prod = ''
        string = '|{:30}|{:30}|{:30}|{:30}|'.format(' '.join(stack), ' '.join(entry), action, prod)
        print(string)


class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]

    def push(self, elm):
        self.s.append(elm)

    def copy(self):
        return self.s.copy()
