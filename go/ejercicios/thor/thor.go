package main

import "fmt"

func Thor(n, m int, h, f, p []float64, d float64) {
	var c int
	for i := 0; i < n; i++ {
		for z := 0; z < n; z++ {
			for x := 0; x < m; x++ {
				if ((h[i] * f[z]) / p[x]) >= d {
					c++
				}
			}
		}
	}
	fmt.Print(c)
	// return c
}
