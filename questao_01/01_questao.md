# [ 01 Exercício ]

> Note: <strong>Dados os valores lógicos A é verdadeiro, B é falsa e C é verdadeira. Qual o valor lógico de cada expressão a seguir?
>
> a) A ^ ( B v C )
>
> b) ( A ^ B ) v C
>
> c) ( A ^ B )' v C
>
> d) A' v ( B' ^ C )

> Seguindo a lógica computacional, como poderia ser resolvido esse problema em forma de um algoritmo funcional? se possível, mostre uma implementação.</strong>

##

### a ) V e (V) -> Verdadeiro 

A conjunção(E) entre A e a disjunção(OU) entre B e C é verdadeira.
 
Na lógica matemática, a conjunção(E) só é verdadeira quando ambas as sentenças são verdadeiras, enquanto a disjunção(OU) 
é verdadeira quando pelo menos uma das sentenças é verdadeira. 
Neste caso, A é verdadeiro e C é verdadeiro, portanto, a expressão A ^ (B v C) é verdadeira.


### b ) F ou V -> Verdadeiro 

A conjunção(E) entre A e B é falsa, e a disjunção(OU) entre C e o resultado da conjunção é verdadeira. 

Na disjunção, é necessário que pelo menos uma das sentenças seja verdadeira. 
Neste caso, C é verdadeiro, portanto a expressão é verdadeira.
 

### c ) V ou V -> Verdadeiro 

A conjunção(E) entre A e B é falsa, logo, a sua negação é o valor lógico verdadeiro. (A ^ B) = Falso | (A ^ B)' = Verdadeiro. 
A disjunção entre o resultado da conjunção(E) e C é verdadeiro.

Na disjunção, é necessário que pelo menos uma das sentenças seja verdadeira. Neste caso, C é verdadeiro, portanto a expressão é verdadeira.
 

### d ) F ou (V e V) -> F ou V -> Verdadeiro 

Sabemos que a negação inverte o valor lógico das sentenças, logo, A' = Falso e B' = Verdadeiro.
A disjunção entre A'(Falso) e o resultado da conjunção entre B'(Verdadeiro) e C(Verdadeiro) é verdadeiro.

Na disjunção, é necessário que pelo menos uma das sentenças seja verdadeira. 
Neste caso, a conjunção (B' ^ C) é verdadeira, portanto a expressão é verdadeira.