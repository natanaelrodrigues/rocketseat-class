package main

import (
	"fmt"
	"math"
	"strconv"
	"time"
)

func main() {
	fmt.Println("Hello, world!")

	// declaração de variáveis
	var nome, sobrenome string
	novoNome := "Aluis"
	var idade = 30

	// usando as variáveis
	nome = "Jose"
	sobrenome = "Rodrigues"

	//types
	var active bool = true
	var y int       // int8, int16 int32 int64
	var x uint      // uint8 uint16 uint32 uint64 uintptr  >> apenas positivos.
	var b byte      // ou int8
	var r rune      // ou int32
	var f float32   // ou float64
	var c complex64 // ou complex128
	var s string

	//constantes
	const minhaConst int = 10

	// convertendo número para string.
	numeroParaString := 10084
	novaString := strconv.FormatInt(int64(numeroParaString), 10)

	fmt.Println(nome, sobrenome, novoNome, idade, active, y, x, b, r, f, c, s, novaString, minhaConst)

	// arrays
	arr := [3]int{2, 10, 978} // o tamanho do array tem que ser constante.
	fmt.Println(arr)

	arrayComLocalDefinido := [10]int{5: 400, 7: 300}
	fmt.Println(arrayComLocalDefinido)

	// Loops
	fmt.Println("++++ TABUADA COM LOOP ++++")
	for i := 0; i < 10; i++ {
		res := i * 10
		fmt.Println("10 x", i, "=", res)
	}

	elements := [10]int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}

	for index, elem := range elements {
		fmt.Println(index, elem)
	}

	for i := range 10 {
		fmt.Println(i + 1)
	}

	// if Condicionals

	if active {
		fmt.Println("Ativo")
	} else {
		fmt.Println("Inativo")
	}

	// criando uma variável dentro de um if.
	if x := math.Sqrt(4); x < 10 {
		fmt.Println(x)
	}

	// switch
	fmt.Println(isWeekend(time.Now()))
}

// retorna se o dia passado é fim de semana.
func isWeekend(x time.Time) bool {
	switch {
	case x.Weekday() > 0 && x.Weekday() < 6:
		return false
	default:
		return true
	}
}
