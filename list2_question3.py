program MatrizTransposta {

1)OPENMOD, (MODULO, MatrizTransposta), (IDLE), (IDLE)

global:
    int A[10,10], n;

functions:

void LerMatriz () {
2)OPENMOD, (FUNCAO, LerMatriz), (IDLE), (IDLE)

local:
    int i, j;

statements:
	write ("Dimensao da matriz quadrada: ");
3)PARAM, (CADEIA, Dimensao da matriz quadrada: ), (IDLE), (IDLE)
4)WRITE, (INT, 1), (IDLE), (IDLE)

	do read (n); while (n < 0);
5)PARAM, (VAR, n), (IDLE), (IDLE)
6)READ, (INT, 1), (IDLE), (IDLE)
7)LT, (VAR, n), (INT, 0), (VAR, ##1)
8)JF, (VAR, ##1), (IDLE), (RÓTULO, 10)
9)JUMP, (IDLE), (IDLE), (ROTULO 5)

	write ("\nElementos da matriz: \n");
10)PARAM, (CADEIA, \nElementos da matriz: \n), (IDLE), (IDLE)
11)WRITE, (INT, 1), (IDLE), (IDLE)

	for (i <- 0; i <= n-1; i <- i+1)
12)ATRIB, (INT, 0), (IDLE), (VAR, i)
13)MENOS, (VAR, n), (INT, 1), (VAR, ##1)
14)LE, (VAR, i), (VAR, ##1), (VAR, ##2)
15)JF, (VAR, ##2), (IDLE), (ROTULO 31)
		for (j <- 0; j <= n-1; j <- j+1)
16)ATRIB, (INT, 0), (IDLE), (VAR, j)
17)MENOS, (VAR, n), (INT, 1), (VAR, ##3)
18)LE, (VAR, j), (VAR, ##3), (VAR, ##4)
19)JF, (VAR, ##4), (IDLE), (ROTULO 13)
            	read (A[i,j]);
20)IND, (VAR, i), (IDLE), (IDLE)
21)IND, (VAR, j), (IDLE), (IDLE)
22)INDEX, (VAR, A), (INT, 2), (VAR, ##5)
23)PARAM, (VAR, ##5), (IDLE), (IDLE)
24)READ, (INT, 1), (IDLE), (IDLE)
25)MAIS, (VAR, j), (INT, 1), (VAR, ##6)
26)ATRIB, (VAR, ##6), (IDLE), (VAR, j)
27)JUMP, (IDLE), (IDLE), (ROTULO 17)
28)MAIS, (VAR, i), (INT, 1), (VAR, ##7)
29)ATRIB, (VAR, ##7), (IDLE), (VAR, i)
30)JUMP, (IDLE), (IDLE), (ROTULO 13)

31)RETURNOP, (IDLE), (IDLE), (IDLE)
}

void EscreverMatriz () {
32)OPENMOD, (FUNCAO, EscreverMatriz), (IDLE), (IDLE)
local:
    int i, j;
statements:
    if (n <= 0) write ("Matriz nula");
33)LE, (VAR, n), (INT, 0), (VAR, ##8)
34)JF, (VAR, ##8), (IDLE), (ROTULO 38)
35)PARAM, (CADEIA, MATRIZ NULA), (IDLE), (IDLE)
36)WRITE, (INT, 1), (IDLE), (IDLE)
37)JUMP, (IDLE), (IDLE), (ROTULO 59)
    else
        for (i <- 0; i <= n-1; i <- i+1) {
38)ATRIB, (INT, 0), (IDLE), (VAR, i)
39)MENOS, (VAR, n), (INT, 1), (VAR, ##9)
40)LE, (VAR, i), (VAR, ##3), (VAR, ##10)
41)JF, (VAR, ##10), (IDLE), (ROTULO 59)
            for (j <- 0; j <= n-1; j <- j+1)
42)ATRIB, (INT, 0), (IDLE), (VAR, j)
43)MENOS, (VAR, n), (INT, 1), (VAR, ##11)
44)LE, (VAR, j), (VAR, ##11), (VAR, ##12)
45)JF, (VAR, ##12), (IDLE), (ROTULO 39)
                write (A[i,j]);
46)IND, (VAR, i), (IDLE), (IDLE)
47)IND, (VAR, j), (IDLE), (IDLE)
48)INDEX, (VAR, A), (INT, 2), (VAR, ##13)
49)PARAM, (VAR, ##13), (IDLE), (IDLE)
50)WRITE, (INT, 1), (IDLE), (IDLE)

51)MAIS, (VAR, j), (INT, 1), (VAR, ##14)
52)ATRIB, (VAR, ##14), (IDLE), (VAR, j)
53)JUMP, (IDLE), (IDLE), (ROTULO 39)
            write ("\n");
54)PARAM, (CADEIA, \n), (IDLE), (IDLE)
55)WRITE, (INT, 1), (IDLE), (IDLE)

56)MAIS, (VAR, i), (INT, 1), (VAR, ##15)
57)ATRIB, (VAR, ##15), (IDLE), (VAR, i)
58)JUMP, (IDLE), (IDLE), (ROTULO 39)
        }
59)RETURNOP, (IDLE), (IDLE), (IDLE)
}

void Trocar (int i, int j) {
60)OPENMOD, (FUNCAO, Trocar), (IDLE), (IDLE)
local:
    int aux;
statements:
    aux <- A[i,j];
61)IND, (VAR, i), (IDLE), (IDLE)
62)IND, (VAR, j), (IDLE), (IDLE)
63)INDEX, (VAR, A), (INT, 2), (VAR, ##16)
64)ATRIB, (VAR, ##16), (IDLE), (VAR, aux)
    A[i,j] <- A[j,i];
65)IND, (VAR, j), (IDLE), (IDLE)
66)IND, (VAR, i), (IDLE), (IDLE)
67)INDEX, (VAR, A), (INT, 2), (VAR, ##17)
68)IND, (VAR, i), (IDLE), (IDLE)
69)IND, (VAR, j), (IDLE), (IDLE)
70)INDEX, (VAR, A), (INT, 2), (VAR, ##18)
71)ATRIBPONT, (VAR, ##17), (IDLE), (VAR, ##18)
    A[j,i] <- aux;
72)IND, (VAR, j), (IDLE), (IDLE)
73)IND, (VAR, i), (IDLE), (IDLE)
74)INDEX, (VAR, A), (INT, 2), (VAR, ##19)
75)ATRIBPONT, (VAR, aux), (IDLE), (VAR, ##19)
76)RETURNOP, (IDLE), (IDLE), (IDLE)
}

main {
77)OPENMOD, (FUNCAO, main), (IDLE), (IDLE)
local:
    int i, j;
statements:
    	call LerMatriz();
CALLOP, (FUNCAO, LerMatriz), (INT, 0), (VAR, ##20)
	write ("\nMatriz original:\n\n");
78)PARAM, (CADEIA, \nMatriz original:\n\n), (IDLE), (IDLE)
79)WRITE, (INT, 1), (IDLE), (IDLE)

    	call EscreverMatriz();
CALLOP, (FUNCAO, EscreverMatriz), (INT, 0), (VAR, ##21)

	if (n > 0)
80)LT, (INT, 0), (VAR, n), (VAR, ##20)
81)JF, (VAR, ##8), (IDLE), (ROTULO 102)
82)PARAM, (CADEIA, MATRIZ NULA), (IDLE), (IDLE)
83)WRITE, (INT, 1), (IDLE), (IDLE)
        for (i <- 0; i <= n-2; i <- i+1)
85)ATRIB, (INT, 0), (IDLE), (VAR, i)

86)MENOS, (VAR, n), (INT, 1), (VAR, ##21)
87)LE, (VAR, i), (VAR, ##21), (VAR, ##22)
88)JF, (VAR, ##22), (IDLE), (ROTULO 102)
            for (j <- i+1; j <= n-1; j <- j+1)
89)ATRIB, (INT, 0), (IDLE), (VAR, j)
90)MENOS, (VAR, n), (INT, 1), (VAR, ##30)
91)LE, (VAR, j), (VAR, ##30), (VAR, ##31)
92)JF, (VAR, ##31), (IDLE), (ROTULO 86)
                call Trocar (i, j);
93)PARAM, (VAR, i), (IDLE), (IDLE)
94)PARAM, (VAR, j), (IDLE), (IDLE)
95)CALLOP, (FUNCAO, EscreverMatriz), (INT, 2), (VAR, ##32)

96)MAIS, (VAR, j), (INT, 1), (VAR, ##14)
97)ATRIB, (VAR, ##14), (IDLE), (VAR, j)
98)JUMP, (IDLE), (IDLE), (ROTULO 86)

99)MAIS, (VAR, i), (INT, 1), (VAR, ##15)
100)ATRIB, (VAR, ##15), (IDLE), (VAR, i)
101)JUMP, (IDLE), (IDLE), (ROTULO 86)

	write ("\nMatriz transposta:\n\n");
102)PARAM, (CADEIA, \nMatriz transposta:\n\n), (IDLE), (IDLE)
103)WRITE, (INT, 1), (IDLE), (IDLE)

	call EscreverMatriz();
104)CALLOP, (FUNCAO, EscreverMatriz), (INT, 0), (VAR, ##20)
105)RETURNOP, (IDLE), (IDLE), (IDLE)
}
}
