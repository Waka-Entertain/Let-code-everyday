package main

import "fmt"

func brokenCalc(X int, Y int) int {
	t := 0
	if X >= Y {
		return X - Y
	}

	for X != Y {
		t++
		if Y % 2 == 0 && X < Y {
			Y /= 2

		} else {
			Y++
		}

	}
	return t
}

func main()  {
	fmt.Println(brokenCalc(5, 8))
}
