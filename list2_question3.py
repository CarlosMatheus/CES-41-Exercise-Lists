program MatrizTransposta {

1)OPENMOD, (MODULO, MatrizTransposta), (IDLE), (IDLE)

global:
    int A[10,10], n;

//2)PARAM, (VAR, A), (IDLE), (IDLE)
//3)PARAM, (VAR, n), (IDLE), (IDLE)

functions:

void LerMatriz () {
local:
    int i, j;

//4)PARAM, (VAR, i), (IDLE), (IDLE)
//5)PARAM, (VAR, j), (IDLE), (IDLE)

statements:
	write ("Dimensao da matriz quadrada: ");

6)WRITE, (CADEIA, Dimensao da matriz quadrada: ), (IDLE), (IDLE)

	do read (n); while (n < 0);

7)PARAM, (VAR, n), (IDLE), (IDLE)
8)READ, (INT, 1), (IDLE), (IDLE)
9)LT, (VAR, n), (INT, 0), (VAR, ##1)
10)JF, (VAR, ##1), (IDLE), (RÓTULO, 7)

	write ("\nElementos da matriz: \n");

11)WRITE, (CADEIA, \nElementos da matriz: \n), (IDLE), (IDLE)

	for (i <- 0; i <= n-1; i <- i+1)
11)ATRIB, (INT, 0), (IDLE), (VAR, i)
12)MENOS, (VAR, n), (INT, 1), (VAR, ##1)
13)LE, (VAR, i), (VAR, ##1), (VAR, ##2)
14)JF, (VAR, ##2), (IDLE), (ROTULO 29)
		for (j <- 0; j <= n-1; j <- j+1)
15)ATRIB, (INT, 0), (IDLE), (VAR, j)
16)MENOS, (VAR, n), (INT, 1), (VAR, ##3)
17)LE, (VAR, j), (VAR, ##3), (VAR, ##4)
18)JF, (VAR, ##4), (IDLE), (ROTULO 12)
            	read (A[i,j]);
19)IND, (VAR, i), (IDLE), (IDLE)
20)IND, (VAR, j), (IDLE), (IDLE)
21)INDEX, (VAR, A), (INT, 2), (VAR, ##5)
22)PARAM, (VAR, ##5), (IDLE), (IDLE)
23)READ, (INT, 1), (IDLE), (IDLE)
24)MAIS, (VAR, j), (INT, 1), (VAR, ##6)
26)ATRIB, (VAR, ##6), (IDLE), (VAR, j)
25)JUMP, (IDLE), (IDLE), (ROTULO 16)
26)MAIS, (VAR, i), (INT, 1), (VAR, ##7)
27)ATRIB, (VAR, ##7), (IDLE), (VAR, i)
28)JUMP, (IDLE), (IDLE), (ROTULO 12)
15)output of JF
}

void EscreverMatriz () {
local:
    int i, j;
statements:
    if (n <= 0) write ("Matriz nula");
    else
        for (i <- 0; i <= n-1; i <- i+1) {
            for (j <- 0; j <= n-1; j <- j+1)
                write (A[i,j]);
            write ("\n");
        }
}

void Trocar (int i, int j) {
local:
    int aux;
statements:
    aux <- A[i,j];
    A[i,j] <- A[j,i];
    A[j,i] <- aux;
}

main {
local:
    int i, j;
statements:

/*	Leitura e escrita da matriz original	*/

    	call LerMatriz();
	write ("\nMatriz original:\n\n");
    	call EscreverMatriz();

/*	Transformacao da matriz em sua transposta  */

	if (n > 0)
        for (i <- 0; i <= n-2; i <- i+1)
            for (j <- i+1; j <= n-1; j <- j+1)
                call Trocar (i, j);

/*	Escrita da matriz transposta	*/

	write ("\nMatriz transposta:\n\n");
	call EscreverMatriz();
}
}
