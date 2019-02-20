package main

import "fmt"

type sort int

func (s *sort) bubbleSort(arr []int) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr) - i - 1; j++ {
			if arr[j] > arr[j + 1] {
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
			}
		}
	}
}

func (s *sort) selectionSort(arr []int) {
	for i := 0; i < len(arr) - 1; i++ {
		m := i
		for j := i + 1; j < len(arr); j++ {
			if arr[m] > arr[j] {
				m = j
			}
			if m != i {
				arr[m], arr[i] = arr[i], arr[m]
			}
		}
	}
}

func (s *sort) quickSort(arr []int, left int, right int) {
	if left > right {
		return
	}
	base := arr[left]
	i, j := left, right
	for i < j {
		for i < j && arr[j] >= base {
			j--
		}
		for i < j && arr[i] <= base {
			i++
		}
		arr[i], arr[j] = arr[j], arr[i]
	}
	arr[left], arr[i] = arr[i], arr[left]
	s.quickSort(arr, left, i - 1)
	s.quickSort(arr, i + 1, right)
}

func main()  {
	arr := []int{2, 4, 1, 5, 3, 9, 8}
	var s sort
	// s.quickSort(arr, 0, len(arr) - 1)
	// s.bubbleSort(arr)
	s.selectionSort(arr)
	fmt.Println(arr)
}
