from stack import Stack
from utils import get_prod_str


class AnalyserLr:

    def __init__(
            self,
            non_terminals=('E', 'T', 'F'),
            terminals=('id', '+', '*', '(', ')', '$'),
    ):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.stack = Stack()
        self.table = {}
        self.state = '0'
        self.action = self.terminals[0]
        self.create_table()
        self.derivations = list()
        self.create_derivations()
        self.entry_idx = 0
        self.entry = ''
        self.goto = None
        self.state = '0'
        self.output = []
        self.actual_value = None
        self.actual_production_idx = None
        self.actual_production = None
        self.accepted = False

    def analyse(self, entry):

        print_lt = []

        if not entry:
            raise Exception('Empty entry')

        self.reset_entry(entry)
        self.stack.push(('0', ''))

        while not self.accepted:
            print_stack = self.stack.copy() # (0)
            print_entry = self.get_cur_entry()
            action = self.get_current_action() # id
            state = self.state # 0
            goto = self.goto # None

            # print(1)
            # print(goto)
            state, action, goto, actual_value = self.update(state, action, goto) # s = 5, acti = *, None, d5

            self.state = state
            self.goto = goto

            print((print_stack, print_entry, self.get_actual_action_str(), goto))
            print_lt.append((print_stack, print_entry, self.get_actual_action_str(), goto))

    def get_actual_action_str(self):
        if self.actual_production:
            return self.actual_value + ' (' + get_prod_str(self.actual_production) + ')'
        else:
            return self.actual_value

    def get_cur_entry(self):
        return self.entry[self.entry_idx:]

    def get_elm_from_table(self, state, action):
        key = state+action
        value = self.table[key]
        return value

    def reset_entry(self, entry):
        self.entry = entry
        self.entry_idx = 0

    def increase_idx(self):
        self.entry_idx += 1

    def get_current_action(self):
        return self.entry[self.entry_idx]

    def update(self, state, action, goto=None):
        self.actual_production_idx = None
        self.actual_production = None

        if goto is None:
            if action is None:
                raise Exception('Goto and action none')
            try:
                key = state + action
            except:
                print(1)
            if key not in self.table:
                raise Exception('Compilation Error: key not in table')
            value = self.table[key]
            self.actual_value = value

            if value == 'act':
                # raise NotImplementedError()
                self.accepted = True
                return state, action, goto, self.actual_value

            elif value[0] == 'd':
                new_state = value[1:]

                self.increase_idx()
                action = self.get_current_action()
                state = new_state
                goto = goto
                self.stack.push((state, self.actual_value))
                return state, action, goto, self.actual_value

            elif value[0] == 'r':
                if value == 'r3':
                    print(1)
                derivation_first_part = self.get_derivation_first_part(value[1:])

                self.actual_production_idx = value[1:]
                self.actual_production = self.derivations[int(value[1:])]

                goto = derivation_first_part

                self.stack.pop()
                state = self.stack.top()[0]
                return state, action, goto, self.actual_value
        else:
            key = state + goto

            while key not in self.table:
                self.stack.pop()
                state = self.stack.top()[0]
                key = state + goto

            value = self.table[key]

            self.actual_value = value
            new_state = value

            state = new_state
            self.stack.push((state, goto))
            goto = None
            return state, action, goto, self.actual_value

    def get_derivation_first_part(self, number_str):
        return self.derivations[int(number_str)][0]

    def create_derivations(self):
        self.derivations = []

        self.derivations.append(None)
        self.derivations.append(('E', ['E', '+', 'T']))
        self.derivations.append(('E', ['T']))
        self.derivations.append(('T', ['T', '*', 'F']))
        self.derivations.append(('T', ['F']))
        self.derivations.append(('F', ['(', 'E', ')']))
        self.derivations.append(('F', ['id']))

    def create_table(self):
        self.table = dict()

        self.table['0'+'id'] = 'd5'
        self.table['4'+'id'] = 'd5'
        self.table['6'+'id'] = 'd5'
        self.table['7'+'id'] = 'd5'

        self.table['1'+'+'] = 'd6'
        self.table['2'+'+'] = 'r2'
        self.table['3'+'+'] = 'r4'
        self.table['5'+'+'] = 'r6'
        self.table['8'+'+'] = 'd6'
        self.table['9'+'+'] = 'r1'
        self.table['10'+'+'] = 'r3'
        self.table['11'+'+'] = 'r5'

        self.table['2'+'*'] = 'd7'
        self.table['3'+'*'] = 'r4'
        self.table['5'+'*'] = 'r6'
        self.table['9'+'*'] = 'd7'
        self.table['10'+'*'] = 'r3'
        self.table['11'+'*'] = 'r5'

        self.table['0'+'('] = 'd4'
        self.table['4'+'('] = 'd4'
        self.table['6'+'('] = 'd4'
        self.table['7'+'('] = 'd4'

        self.table['2'+')'] = 'r2'
        self.table['3'+')'] = 'r4'
        self.table['5'+')'] = 'r6'
        self.table['8'+')'] = 'd11'
        self.table['9'+')'] = 'r1'
        self.table['10'+')'] = 'r3'
        self.table['11'+')'] = 'r5'

        self.table['1'+'$'] = 'act'
        self.table['2'+'$'] = 'r2'
        self.table['3'+'$'] = 'r4'
        self.table['5'+'$'] = 'r6'
        self.table['9'+'$'] = 'r1'
        self.table['10'+'$'] = 'r3'
        self.table['11'+'$'] = 'r5'

        self.table['0'+'E'] = '1'
        self.table['4'+'E'] = '8'

        self.table['0'+'T'] = '2'
        self.table['4'+'T'] = '2'
        self.table['6'+'T'] = '9'

        self.table['0'+'F'] = '3'
        self.table['4'+'F'] = '3'
        self.table['6'+'F'] = '3'
        self.table['7'+'F'] = '10'


















