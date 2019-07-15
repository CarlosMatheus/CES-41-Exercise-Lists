from production_table import ProductionTable
from utils import vertical_bar, epsilon


terminals = [';', 'int', 'real', 'ID', ',', '{', '}', '=', '+', '(', ')', 'CTE', '*']
non_terminals = ['Prog', 'Decls', 'CmdComp', 'Declaracao', 'LDaux', 'Tipo', 'ListId', 'LIaux', 'ListCmd', 'Comando', 'LCaux', 'CmdAtrib', 'Expressao', 'Termo', 'Eaux']
productions = [
    ('Prog', ['Decls', 'CmdComp']),
    ('Decls', ['Declaracao', 'LDaux']),
    ('LDaux', [epsilon, vertical_bar, 'Decls']),
    ('Declaracao', ['Tipo', 'ListId', ';']),
    ('Tipo', ['int', vertical_bar, 'real']),
    ('ListId', ['ID', 'LIaux']),
    ('LIaux', [epsilon, vertical_bar, ',', 'ListId']),
    ('CmdComp', ['{', 'ListCmd', '}']),
    ('ListCmd', ['Comando', 'LCaux']),
    ('LCaux', [epsilon, vertical_bar, 'ListCmd']),
    ('Comando', ['CmdComp', vertical_bar, 'CmdAtrib']),
    ('CmdAtrib', ['ID', '=', 'Expressao', ';']),
    ('Expressao', ['Termo', 'Eaux']),
    ('Eaux', [epsilon, vertical_bar, '+', 'Expressao']),
    ('Termo', ['(', 'Expressao', ')', vertical_bar, 'ID', vertical_bar, 'CTE']),
]

production_table = ProductionTable(terminals, non_terminals, productions)

print(production_table.get_first())
print(production_table.get_second())
production_table.print_first()
production_table.print_second()
production_table.build_production_table()
production_table.print_table()
