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
        def bfs(roots: List[TreeNode]): List[List[Int]] = 
            if roots.isEmpty then Nil: List[List[Int]]
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
                nums::bfs(newRoots)
        bfs(List(root)).dropRight(1)
    }
}