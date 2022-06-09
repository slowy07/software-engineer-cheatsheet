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
