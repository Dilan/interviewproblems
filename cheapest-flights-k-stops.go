package main
import "fmt"
import "math"

type Node struct {
    Num int
	Price int
    Visited bool
    Dest []*Node
}

func createGraph(flights [][]int) map[int]*Node  {

    graph := make(map[int]*Node)
    for _, item := range(flights) {
        src, dest, price := item[0], item[1], item[2]

		_, sOk := graph[src]
        _, dOk := graph[dest]
        if sOk == false {
			var arr []*Node
			graph[src]  = &Node{ Num:src, Dest:arr, Price: math.MaxInt32 }
		}
        if dOk == false {
			var arr []*Node
			graph[dest] = &Node{ Num:dest, Dest:arr, Price: price }
		}

        graph[src].Dest = append(graph[src].Dest, graph[dest])
    }

    return graph
}
func start(i int, dst int, K int, graph map[int]*Node) {

	// fmt.Print(graph[i])

	if i == dst {
		fmt.Println("arive to destination...")
		return
	}

	if K <= 0 {
		fmt.Println("K is zero ...")
		return
	}

	// return


	for _, node := range(graph[i].Dest) {

		fmt.Println(node)
		if node.Visited == true {
			continue
		}

		node.Visited = true

		if node.Price > graph[i].Price {
			node.Price = graph[i].Price
			start(node.Num, dst, K-1, graph)
		}
    }
}

func findCheapestPrice(n int, flights [][]int, src int, dst int, K int) int {

    graph := createGraph(flights)

	fmt.Println("Destination id: ", dst)

    // fmt.Println(graph)
    start(src, dst, K, graph)

	fmt.Println("Destination price is: ", graph[dst].Price)

    return 1
}

func main() {

	n := 3
	flights := [][]int{{0,1,100},{1,2,120},{0,2,500}}
	src, dst := 0, 2
	k := 1
	res := findCheapestPrice(n, flights, src, dst, k)

	fmt.Println(res)
}
