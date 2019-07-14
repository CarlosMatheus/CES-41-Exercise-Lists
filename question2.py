from analyser import Analyser

analyser = Analyser()
analyser.analyse(['id', '*', '(', '(', 'id', '+', 'id', ')', '*', '(', 'id', '*', '(', 'id', '+', 'id', ')', ')', ')', '$'])
