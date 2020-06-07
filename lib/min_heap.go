// https://leetcode.com/problems/queue-reconstruction-by-height/

// Suppose you have a random list of people standing in a queue.
// Each person is described by a pair of integers (h, k), where h is the height
// of the person and k is the number of people in front of this person who have
// a height greater than or equal to h. Write an algorithm to reconstruct the queue.

// Input:
// 		[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
// Output:
// 		[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

package main
import "fmt"

func heapify(list [][]int, i int) {
	    ldx, rdx := (i * 2) + 1, (i * 2) + 2
	    min := i

	    if ldx < len(list) {
			if (list[ldx][0] == list[min][0] && list[ldx][1] < list[min][1]) ||
			   (list[ldx][0] < list[min][0]) {
				min = ldx
			}
		}
		if rdx < len(list) {
			if (list[rdx][0] == list[min][0] && list[rdx][1] < list[rdx][1]) ||
			   (list[rdx][0] < list[min][0]) {
				min = rdx
			}
		}
	    if min != i {
	        list[min], list[i] = list[i], list[min]
	        heapify(list, min)
		}
}

func pop(list [][]int) ([]int, [][]int) {
	item := list[0]
	list[0], list = list[len(list)-1], list[0:len(list)-1]
	heapify(list, 0)
	return item, list
}

func reconstructQueue(people [][]int) [][]int {
	// build Min Heap
	middle := len(people) / 2 - 1
	for i := middle; i >= 0; i-- {
		heapify(people, i)
	}

	var item []int
	queue := make([][]int, len(people))
	for ; len(people) > 0; {
		item, people = pop(people)

		k := item[1]
		for i:=0; i<len(queue); i++ {
            if k != -1 {
                if (len(queue[i]) > 0 && queue[i][0] >= item[0]) || len(queue[i]) == 0 {
                    k--
                }
            }
            if k == -1 && len(queue[i]) == 0 {
                queue[i] = item
                break
            }
        }
	}
	return queue
}

func main() {

	people := [][]int{
		{7,0},{4,4},{7,1},{5,0},{6,1},{5,2},
	}
	queue := reconstructQueue(people)

	fmt.Println("Input :", people)
	fmt.Println("Output:", queue)
}
