package main

func main() {
	n := 4
	m := 4
	h := [n]float64{10, 14, 0, 1}
	f := [n]float64{25, 37, 48, 54}
	p := [m]float64{3, 7, 9, 1000}
	var d float64 = 10

	thor(n, m, h, f, p, d)
}
