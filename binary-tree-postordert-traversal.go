/*
[left middle right] - in-order
[middle left right] - pre-order
[left right middle] - post-order

Given a binary tree, return the postorder traversal of its nodes' values.
{1,#,2,3},

   1
    \
     2     output [3,2,1]
    /
   3

{10,12,5,3,4,11,2,#,#,6,7,#,#,#,8}

       10
    /     \
  12       5
 / \     /  \     output [3,6,7,4,12,11,8,2,5,10]
3   4   11   2
   / \       \
  6  7       8


*/
package main

import (
    "fmt"
    "strconv"
    "strings"
)

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}



func isLeaf(node *TreeNode) bool {
    return (node.Left == nil) && (node.Right == nil)
}

func postorderTraversal(root *TreeNode) []int {
    result := []int{}

    if root == nil {
        return result
    }

    stack := []*TreeNode{root}
    var node *TreeNode
    for len(stack) > 0 {
        node, stack = stack[0], stack[1:]

        if isLeaf(node) {
            result = append(result, node.Val)
            continue
        }

        stack = append([]*TreeNode{ node }, stack...)
        if node.Right != nil {
            stack = append([]*TreeNode{ node.Right }, stack...)
        }
        if node.Left != nil {
            stack = append([]*TreeNode{ node.Left }, stack...)
        }

        // make current Node just a (visited) Leaf
        node.Left = nil
        node.Right = nil
    }
    return result
}

func buildTree(treeList []string) TreeNode {
    rootVal, _ := strconv.Atoi(treeList[0])
    root := TreeNode{Val:rootVal}
    rootIdx := 0
    rootList := []*TreeNode{&root}

    for i:= 1; i < len(treeList); i++ {
        isLeft := (i % 2) != 0

        if treeList[i] != "#" {
            nodeVal, _ := strconv.Atoi(treeList[i])
            node := TreeNode{Val:nodeVal}
            if isLeft {
                rootList[rootIdx].Left = &node
            } else {
                rootList[rootIdx].Right = &node
            }
            rootList = append(rootList, &node)
        }

        if !(isLeft) {
            rootIdx += 1
        }
    }
    return root
}

func main() {

    r1 := buildTree(strings.Split("1,#,2,3", ","))
    fmt.Println(postorderTraversal(&r1))

    r2 := buildTree(strings.Split("10,12,5,3,4,11,2,#,#,6,7,#,#,#,8", ","))
    fmt.Println(postorderTraversal(&r2))

}
