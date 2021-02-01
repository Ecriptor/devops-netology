package main
import "fmt"

func main() {
	fmt.Print("Расстояние в метрах: ")
	var meter float64
	fmt.Scanf("%f", &meter )

	var ft float64
	ft = meter / 0.3048

	fmt.Println("Расстояние в футах: ")
	fmt.Println(ft)
}
