package main

import "fmt"

func permute(nums []int) [][]int  {
	var res [][]int

	if len(nums) == 1 {
		return [][]int{nums}
	}

	for i := 0; i < len(nums); i++ {
		nums[0], nums[i] = nums[i], nums[0]
		temp := permute(nums[1:])
		for _, t := range temp {
			res = append(res, append([]int{nums[0]}, t...))
		}
		nums[i], nums[0] = nums[0], nums[i]
	}
	return res
}

func main() {
	fmt.Println(permute([]int{1, 2, 3}))
}
