class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1
        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
            """
            A p0 = 1
            B p1 = 1n0
            C p2 = n1*p1 = 1n0n1
            D p3 = n2p2 = 1n0n1n2
            E p4 = n3p3 = 1n0n1n2n3
            """
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]
            """
            E s4 = 1
            D s3 = n4*s4 = n4*1
            C s2 = n3*s3 = n3n4*1
            B s1 = n2*s2 = n2n3n4*1
            A s0 = n1*s1 = n1n2n3n4*1
            """
        for i in range(n):
            res[i] = pref[i] * suff[i]
 
        return res