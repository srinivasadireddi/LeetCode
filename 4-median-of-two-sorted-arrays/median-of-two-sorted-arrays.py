class Solution:
    def findMedianSortedArrays(self, arr1: list[int], arr2: list[int])->float:
        n1 = len(arr1)
        n2 = len(arr2)
        n=n1+n2

        if n1>n2:
            return self.findMedianSortedArrays(arr2, arr1)
        
        low = 0 #0 elements
        high = n1 

        left = (n1+n2+1)//2

        while low<=high:
            mid1 = (low+high)//2 #these many elements from n1 on the left block
            mid2 = left - mid1

            # if mid1>0:
            #     l1=arr1[mid1-1]
            # else:
            #     l1=float("-inf")
            
            l1=arr1[mid1-1] if mid1>0 else float("-inf")
            l2=arr2[mid2-1] if mid2>0 else float("-inf")
            
            r1=arr1[mid1] if mid1<n1 else float("inf")
            r2=arr2[mid2] if mid2<n2 else float("inf")

            if(l1<=r2 and l2<=r1):
                #success!
                if(n%2==0):
                    return ( max(l1,l2)+min(r1,r2) )/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=mid1-1
            elif l2>r1:
                low=mid1+1
        
        # return 0.0

# #Online solution with explanation
# class Solution:
#     def findMedianSortedArrays(self, arr1: list[int], arr2: list[int]) -> float:

#         # MEDIAN 
#         # ODD NUMBER OF ELEMENTS  -> MIDDLE ELEMENT
#         # EVEN NUMBER OF ELEMENTS -> (MID1 + MID2) / 2

#         # EX:
#         # ARR1[] -> 1 3 4 7 10 12
#         # ARR2[] -> 2 3 6 15

#         # COMBINED VERSION
#         # 1 2 3 3 4  | 6 7 10 12 15 -> SYMMETRICAL LINE
#         # 5 ON LEFT  | 5 ON RIGHT

#         # OUT OF THIS 5 ON LEFT,
#         # HOW MANY ARE COMING FROM ARR1 AND HOW MANY FROM ARR2
#         # ARR1 -> 1 3 4 [3 ELEMENTS]
#         # ARR2 -> 2 3   [2 ELEMENTS]

#         # WHOLE IDEA COMES TO FORMULATING THE CORRECT SORTED LEFT HALF
#         # INCLUDING HOW MANY FROM ARR1 AND HOW MANY FROM ARR2 -> LEFT HALF

#         # WE CAN TRY TAKING 0 ELEMENTS FROM ARR1 TO ALL ELEMENTS FROM ARR 1
#         # I.E. 0 ... ARR1.SIZE()

#         # TRY TAKING 1 FROM ARR1 REST FROM ARR2 
#         #          | 1 3 4 7 10 12
#         # 2 3 6 15 |
#         # NOT SORTED, NOT POSSIBLE -> NEED 5 IN FIRST HALF, NOT EVEN POSSIBLE

#         # TRY TAKING 1 FROM ARR1 REST FROM ARR2 
#         # 1        | 3 4 7 10 12
#         # 2 3 6 15 |
#         # NOT SORTED, NOT POSSIBLE

#         # TRY TAKING 2 FROM ARR1 REST FROM ARR2 
#         # 1 3     |  4 7 10 12
#         # 2 3 6   |   15
#         # NOT SORTED, NOT POSSIBLE

#         # TRY TAKING 3 FROM ARR1 REST FROM ARR2 
#         # 1 3 4  |  7 10 12
#         # 2 3    |  6 15
#         # SORTED, POSSIBLE

#         # TRY TAKING 4 FROM ARR1 REST FROM ARR2 
#         # 1 3 4 7 |  10 12
#         # 2       |  3 6 15
#         # NOT SORTED, NOT POSSIBLE

#         # TRY TAKING 5 FROM ARR1 REST FROM ARR2 
#         # 1 3 4 7 10 |  12
#         #           |   2 3 6 15
#         # NOT SORTED, NOT POSSIBLE

#         # OBSERVATION OF SEARCH SPACE, NO OF ELEMENTS FROM ARR 1
#         # 0   1   2   3    4   5
#         # NO  NO  NO  YES  NO  NO

#         # THERE WILL BE ONLY 1 VALID CONFIGURATION

#         # TO DECIDE IF .. FROM ARR1 AND .. FROM ARR2 IS VALID SYMMETRY OR NOT
#         # EX: 

#         # NOTE: ARR1 AND ARR2 LINES WILL BE SORTED IN THEMSELVES

#         # 4 ARR1, 1 ARR2 
#         # 1 3 4 7 |  10 12
#         # 2       |  3 6 15
#         # NOT SORTED, NOT POSSIBLE
#         # HERE, 2 < 10 OK, 7 > 3 NOT OK.
#         # TAKING MORE ELEMENTS FROM ARR1 NOT POSSIBLE, TAKE LESS FROM ARR1

#         # 3 ARR1, 2 ARR2
#         # 1 3 4[l1]  |  7[r1] 10 12
#         # 2 3[l2]    |  6[r2] 15
        
#         # SORTED, POSSIBLE
#         # HERE, 4 < 6 OK, 3 < 7 OK.
#         # ONLY VALID CONFIGURATION
#         # MEDIAN CALCULATION,
#         # ODD NO OF ELEMENTS  -> 
#         # NOTE:
#         # EX: n1 = 2, n2 = 3
#         # SYMMETRY COULD BE 3 | 2 OR 2 | 3, MEANS EITHER 3 FROM ARR1 OR 2 FROM ARR1
#         # TAKE 3 | 2 SYMMETRY BY TAKING (n1 + n2 + 1) / 2, ELEMENTS IN LEFT HALF
#         # SO MEDIAN WOULD BE MAX(l1, l2)
#         # EVEN NO OF ELEMENTS -> (MID1 + MID2) / 2
#         # MID1 = MAX(l1, l2), MID2 = MIN(r1, r2)
#         # MEDIAN -> (MID1 + MID2) / 2.0

#         # 2 ARR1, 3 ARR2
#         # 1 3     |  4 7 10 12
#         # 2 3 6   |   15
#         # NOT SORTED, NOT POSSIBLE
#         # HERE, 3 < 15 OK, 6 < 4 NOT OK.
#         # TAKING LESS ELEMENTS FROM ARR1 NOT POSSIBLE, TAKE MORE ELEMENTS FROM ARR1

#         # HOW TO DECIDE WHICH HALF TO ELIMINATE?
#         # ANY CASE, l1 > r2 -> TAKE LESS ELEMENTS FROM ARR1  -> TRIM RIGHT HALF
#         # ANY CASE, l2 > r1 -> TAKE MORE ELEMENTS FROM ARR 1 -> TRIM LEFT HALF

#         # DO BINARY SEARCH ON SMALLER ARRAY TO REDUCE TC 

#         n1 = len(arr1)
#         n2 = len(arr2)

#         # PERFORM BS ON SMALLER SIZED ARRAY
#         if n1 > n2:
#             return self.findMedianSortedArrays(arr2, arr1)

#         # 0 ELEMENTS FROM ARR1
#         low = 0

#         # ALL n1 ELEMENTS FROM ARR1
#         high = n1

#         # TOTAL NUMBER OF ELEMENTS FORM BOTH ARRAYS
#         n = n1 + n2

#         # NO OF ELEMENTS IN LEFT HALF
#         left = (n1 + n2 + 1) // 2

#         while low <= high:

#             # SYMMETRY LINE FOR ARR1
#             mid1 = low + (high - low) // 2

#             # SYMMETRY LINE FOR ARR2
#             # EX:
#             # IF low = 0, high = 6
#             # mid1 = 3
#             # I.E. ELEMENTS FROM 0 ... mid1 - 1 FROM ARR1
#             # SO, left = 6
#             # mid2 = left - mid1 -> 6 - 3 = 3
#             # I.E. ELEMENTS FROM 0 ... mid2 - 1 FROM ARR2 
#             # EVENTUALLY 3 FROM ARR1, AND 3 FROM ARR2 
#             mid2 = left - mid1

#             # TAKE DEFAULT VALUES AS INT_MIN,
#             # TO MAKE THE COMPARION TRUE IN CASE VALUES ARE ABSENT
#             # IN CASE 0 ELEMS FROM ARR1 OR 0 ELEMS FROM ARR2 IN LEFT HALF OF SYMMETRY
#             l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
#             l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')

#             # TAKE DEFAULT VALUES AS INT_MAX,
#             # IN CASE 0 ELEMS FROM ARR1 OR 0 ELEMS FROM ARR2 IN RIGHT HALF OF SYMMETRY
#             r1 = arr1[mid1] if mid1 < n1 else float('inf')
#             r2 = arr2[mid2] if mid2 < n2 else float('inf')

#             # ONLY VALID SYMMETRY FOUND
#             if l1 <= r2 and l2 <= r1:
#                 if n % 2 == 1:
#                     return max(l1, l2)
#                 else:
#                     return (max(l1, l2) + min(r1, r2)) / 2.0
#             elif l1 > r2:
#                 # TAKE LESS ELEMENTS FROM ARR1
#                 high = mid1 - 1
#             else:
#                 # TAKE MORE ELEMENTS FORM ARR2
#                 low = mid1 + 1

#         return 0.0