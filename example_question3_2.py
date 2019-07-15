from production_table import ProductionTable
from utils import vertical_bar, epsilon


terminals = ['i', 'b', 'a', 'e']
non_terminals = ['S', "S'"]
productions = [
    ('S', ['i', 'b', 'S', "S'", vertical_bar, 'a']),
    ("S'", ['e', 'S', vertical_bar, epsilon]),
]

production_table = ProductionTable(terminals, non_terminals, productions)

print(production_table.get_first())
print(production_table.get_second())
production_table.print_first()
production_table.print_second()
production_table.build_production_table()
production_table.print_table()
