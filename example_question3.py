from production_table import ProductionTable
from utils import vertical_bar, epsilon


terminals = ['+', '*', '(', ')', 'id']
non_terminals = ['E', "E'", 'T', "T'", 'F']
productions = [
    ('E', ['T', "E'"]),
    ("E'", ['+', 'T', "E'", vertical_bar, epsilon]),
    ('T', ['F', "T'"]),
    ("T'", ['*', 'F', "T'", vertical_bar, epsilon]),
    ('F', ['(', 'E', ')', vertical_bar, 'id'])
]

production_table = ProductionTable(terminals, non_terminals, productions)

print(production_table.get_first())
