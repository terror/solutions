package main

import ("fmt"; "strings")

func main() {


	var n int
	fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		var x int;
		fmt.Scanln(&x)

		mp := make(map[int]int)
		var line string
		fmt.Scanln(&line)

		for j := range line {
			mp[line[j]]++
		}

		for key, val := range mp {
			if val == 1 {
				fmt.Sprintf("Case #%d: %d", key, i + 1)
			}
		}
	}
}
