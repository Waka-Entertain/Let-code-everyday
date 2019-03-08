package main

import (
	"fmt"
	"regexp"
)

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	s := ""
	singleDigit := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
	tenDigit := []string{"Ten", "Eleven", "Twelve", "Thirteen",
	"Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
	tyDigit := []string{"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
	if num >= 1000000000 {
		s += numberToWords(num / 1000000000) + " Billion "
		num -= num / 1000000000 * 1000000000
	}
	if num >= 1000000 {
		s += numberToWords(num / 1000000) + " Million "
		num -= num / 1000000 * 1000000
	}
	if num >= 1000 {
		s += numberToWords(num / 1000) + " Thousand "
		num -= num / 1000 * 1000
	}
	if num >= 100 {
		s += singleDigit[num / 100 - 1] + " Hundred "
		num -= num / 100 * 100
	}
	if num >= 20 {
		s += tyDigit[num / 10 - 2] + " "
		num -= num / 10 * 10
	} else if num >= 10 {
		s += tenDigit[num - 10]
		num -= num
	}
	if num > 0 {
		s += singleDigit[num - 1]
		num -= num
	}
	reg, _ := regexp.Compile(`(\s*$)`)
	return reg.ReplaceAllString(s, "")
}

func main()  {
	fmt.Println(numberToWords(1234567890))
}
