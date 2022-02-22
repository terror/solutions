package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		var a string
		var b string

		fmt.Scanln(&a);
		fmt.Scanln(&b);

		var ret string

		for j := 0; j < len(a); j++ {
			if a[j] != b[j] {
				ret += "*"
			} else {
				ret += "."
			}
		}

		fmt.Println(a)
		fmt.Println(b)
		fmt.Println(ret + "\n")
	}
}
