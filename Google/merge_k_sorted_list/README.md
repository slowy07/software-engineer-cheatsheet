# merge k sorted lists

You are given an array of ``k`` linked-lists ``lists``, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


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

```
Input: lists = [[]]
Output: []
```

```python
class ProblemSolve:
    def merge_k_list(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) > 0:
            if not any(lists):
                return
            
        hp = []
        for i, lst in enumerate(lists):
            curr = lst
            j = 2
            while curr:
                hp.append((curr.val, j, i))
                curr = curr.next
                j += 1
        
        heapq.heapify(hp)
        temp = ListNode(heapq.heappop(hp)[0])
        ans_head = temp

        while hp:
            temp.next = ListNode(heapq.heappop(hp)[0])
            temp = temp.next
        
        return ans_head
```