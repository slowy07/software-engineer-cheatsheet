# merge k sorted lists

You are given an array of k linked-lists ``lists``, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and ``return`` it.


```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

```
Input: lists = []
Output: []
```

```python
class ProblemSolve:
    def merge_k_sorted_lists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        q = []
        sent = ListNode()

        for l in list:
            node = l
            while node:
                heapq.heappush(q, node.val)
                node = node.next

        if q:
            p = heapq.heappop(q)
            node = ListNode(val=p)
            sent.next = node

        while q:
            p = ListNode(val=heapq.heappop(q))
            node.next = p
            node = p

        return sent.next
```