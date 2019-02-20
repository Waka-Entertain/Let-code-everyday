package main

import "fmt"

func numFriendRequests(ages []int) int {
	countMap := make(map[int]int)
	for _, age := range ages{
		if _, ok := countMap[age]; ok {
			countMap[age] += 1
		} else {
			countMap[age] = 1
		}
	}

	ans := 0

	for ageA, countA := range countMap {
		for ageB, countB := range countMap {
			if float64(ageA) * 0.5 + 7 >= float64(ageB) {
				continue
			}
			if ageA < ageB {
				continue
			}
			ans += countA * countB
			if ageA == ageB {
				ans -= countA
			}
		}
	}
	return ans
}

func main()  {
	fmt.Println(numFriendRequests([]int{20,30,100,110,120}))
	fmt.Println(numFriendRequests([]int{16, 16, 16, 16}))
	//fmt.Println(numFriendRequests([]int{16,17,18}))
}
