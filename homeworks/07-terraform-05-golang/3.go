package main
import "fmt"

func main() {
    var array []int
    for i := 1; i <= 100; i++ {
        if i%3 == 0 {
		array = append(array, i)
        }
    }
    fmt.Println("В диапазоне от 1 до 100 делятся на 3 без остатка следующие числа:")
    fmt.Printf("%v\n",array)
}
