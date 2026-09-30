class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        top_k_num = []  # liste de nombre croissé par ordre décroissant de num_count

        def insert_num(num, top_k_num=top_k_num, num_count=num_count):
            for i in range(len(top_k_num)):
                if num_count[num] > num_count[top_k_num[i]]:
                    top_k_num = top_k_num[:i] + [num] + top_k_num[i:]
                    return top_k_num
            top_k_num.append(num)
            return top_k_num

        def update_top_k(num, top_k_num=top_k_num, num_count=num_count, k=k):
            if len(top_k_num) < k:
                top_k_num = insert_num(num, top_k_num=top_k_num, num_count=num_count)
            elif num_count[num] > num_count[top_k_num[-1]]:
                top_k_num.pop(-1)
                top_k_num = insert_num(num, top_k_num=top_k_num, num_count=num_count)
            
            return top_k_num

        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else :
                num_count[num] += 1

        for num in num_count.keys():
            top_k_num = update_top_k(num, top_k_num=top_k_num, num_count=num_count, k=k)

        return top_k_num