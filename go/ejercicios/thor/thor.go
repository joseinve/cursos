package thor

func Thor(n, m int, h, f, p, d float64) {
	var c int
	for i := 0; i < n; i++ {
		for z := 0; z < n; z++ {
			for x := 0; x < m; x++ {
				if ((h * f) / p) >= d {
					c++
				}
			}
		}
	}
	// return c
}
