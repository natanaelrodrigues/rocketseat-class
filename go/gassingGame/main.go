package main

import (
	"bufio"
	"fmt"
	"math/rand/v2"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Jogo da Adivinhação")
	fmt.Println("Um número aleatório será sorteado. Tente acertar. O número é um inteiro entre 0 e 100")

	// leitura da digitação do usuário
	scanner := bufio.NewScanner(os.Stdin)
	chutes := [10]int64{}

	x := rand.Int64N(101)

	for i := range chutes {
		fmt.Println("Qual é o seu chute?")
		scanner.Scan()
		chute := scanner.Text()
		chute = strings.TrimSpace(chute)

		chuteInt, err := strconv.ParseInt(chute, 10, 64)

		if err != nil {
			fmt.Println("O seu chute tem que ser um número inteiro")
			return
		}

		chutes[i] = chuteInt

		switch {
		case chuteInt < x:
			fmt.Println("Você errou. O número sorteado é MAIOR que", chuteInt)
		case chuteInt > x:
			fmt.Println("Você errou. O número sorteado é MENOR que", chuteInt)
		case chuteInt == x:
			fmt.Printf(
				"PARABÉNS! o número era: %d\n"+
					"Você acertou em %d tentativas.\n"+
					"Essas foram as suas tentativas %v\n", x, i+1, chutes[:i],
			)
			return
		}

	}

	fmt.Printf(
		"Infelizente você não acertou o número, que era %d\n"+
			"Você teve 10 tentativas.\n"+
			"Essas foram as suas tentativas %v\n", x, chutes,
	)
}
