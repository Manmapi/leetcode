/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def levelOrder(root: TreeNode): List[List[Int]] = {
        @scala.annotation.tailrec
        def bfs(roots: List[TreeNode], accumulate: List[List[Int]]): List[List[Int]] = 
            if roots.isEmpty then accumulate
            else 
                val nums = roots.foldLeft(List(): List[Int])((acc, x) => 
                   x match 
                    case t: TreeNode => t.value :: acc
                    case null  => acc 
                )
                val newRoots = roots.foldLeft(List(): List[TreeNode])((acc, x) => 
                    x match 
                        case t: TreeNode => List(t.left, t.right) ++ acc
                        case null  => acc 
                ).reverse
                bfs(newRoots, nums::accumulate)
        bfs(List(root), Nil: List[List[Int]]).drop(1).reverse
    }
}