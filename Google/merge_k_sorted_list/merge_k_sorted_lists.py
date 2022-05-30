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
