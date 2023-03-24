package main

import (
	"fmt"

	"github.com/joseinve/go/funciones/nums"
)

func main() {
	a := 5
	b := 6

	fmt.Printf("%d is even %v?\n", a, nums.Even(a))
	fmt.Printf("%d is odd %v?\n", b, nums.Odd(b))
}
