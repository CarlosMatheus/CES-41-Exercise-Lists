from production_table import ProductionTable
from utils import vertical_bar, epsilon


terminals = ['id', '+', '*', '(', ')']
non_terminals = ["E'", 'E', 'T', 'F']
productions = [
    ("E'", ['E']),
    ('E', ['E', '+', 'T', vertical_bar, 'T']),
    ('T', ['T', '*', 'F', vertical_bar, 'F']),
    ('F', ['(', 'E', ')']),
    ('F', ['id']),
]

production_table = ProductionTable(terminals, non_terminals, productions)

print(production_table.get_first())
print(production_table.get_second())
production_table.print_first()
production_table.print_second()
production_table.build_production_table()
production_table.print_table()
