package main

import "fmt"

func twoSum(nums []int, target int) []int {
	lookup := make(map[int]int)
	for i, num := range nums {
		if j, ok := lookup[target-num]; ok {
			return []int{j, i}
		}
		lookup[nums[i]] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2,7,11,15}, 9))
}
