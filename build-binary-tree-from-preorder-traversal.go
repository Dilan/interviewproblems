// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main
import "fmt"
import "strconv"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}


func bstFromPreorder(preorder []int) *TreeNode {

    var top *TreeNode
    root := TreeNode{ Val:preorder[0] }

	queue := make([]*TreeNode,0,len(preorder))
    queue = append(queue,  &root)

    for _, v := range(preorder[1:]) {

        if v < queue[ len(queue)-1 ].Val {
            queue[len(queue)-1].Left = &TreeNode{Val:v}
            queue = append(queue,  queue[len(queue)-1].Left)
        } else {
            top, queue = queue[len(queue)-1], queue[:len(queue)-1]
            for ; len(queue) > 0; {
                if (queue[len(queue)-1].Val > v) { break }
                top, queue = queue[len(queue)-1], queue[:len(queue)-1]
            }
            top.Right = &TreeNode{Val:v}
            queue = append(queue,  top.Right)
        }
    }
    return &root
}



func main() {
    arr := []int{8,5,1,7,10,12}

	root := bstFromPreorder(arr)

	fmt.Println(" " + strconv.Itoa(root.Val))
	fmt.Println(root.Left.Val, root.Right.Val)
	fmt.Println("....")
}
