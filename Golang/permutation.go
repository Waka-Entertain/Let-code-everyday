package main

import "fmt"

func Permutation(arr []string) []string {
	var ans []string
	n := len(arr)
	if n == 1 {
		return []string{arr[0]}
	}

	for i := 0; i < n; i++ {
		arr[0], arr[i] = arr[i], arr[0]
		res := Permutation(arr[1:])
		for _, s := range res {
			ans = append(ans, arr[0] + s)
		}
		arr[i], arr[0] = arr[0], arr[i]

	}

	return ans
}

func main() {
	fmt.Println(Permutation([]string{"a", "b", "c"}))
}
