package main

import "fmt"

func main() {
	set := make(map[int]bool)

	for i := 0; i < 10; i++ {
		var x int
		fmt.Scanln(&x)
		set[x%42] = true
	}

	fmt.Println(len(set))
}
