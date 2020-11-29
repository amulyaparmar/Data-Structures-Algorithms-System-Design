# Data Structures and Algorithms
This is my personal Data Structures and Algorithms study guide for coding interviews.  It is based off practice sites, articles, papers, online courses, and the roughly 500 Leetcode problems I've experienced.  

## Table of Contents
- Dynamic Programming
- Sorts / Searches
- Graphs 
- Trees
- Strings / Arrays
- Intervals
- Pathing
- Bits
- Other
- Backtracking
- Linked Lists
- Stacks / Queues


### 1. [Dynamic Programming](https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews)

**Follow [this](https://tinyurl.com/vmmaxbe) golden rule to approach any DP problem.**

<details><summary>Leetcode problems with solutions and tutorials/videos</summary>
<p>

| #  | Title | Solution | Tutorial | Level | Remarks |
| --- | --- | --- | --- | --- | --- |
|01| [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/submissions/)| [Python](https://tinyurl.com/wu6rdaw/53_Maximum_Subarray.py)| [Vid 1](https://tinyurl.com/wnjuna5), [Algoexpert.io](https://tinyurl.com/vqcznww) | Easy | Kadane's Algorithm |
|02| [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)| [Python](https://tinyurl.com/wu6rdaw/518_Coin_Change_2.py)| **[educative.io](https://tinyurl.com/ro6das2)**, [Vid 1](https://tinyurl.com/wj5xxmw), [codinginterviewclass.com](https://tinyurl.com/urd4fg5), [Algoexpert.io](https://tinyurl.com/rv4r9e6) | Medium | Unbounded Knapsack |
|03| [322. Coin Change](https://leetcode.com/problems/coin-change/solution/)| [Python](https://tinyurl.com/wu6rdaw/322_Coin_Change.py)| **[educative.io](https://tinyurl.com/w7t6jpo)**, [Vid 1](https://tinyurl.com/qlqrz6z), [Algoexpert.io](https://tinyurl.com/sv32o4z) | Medium | Unbounded Knapsack |
|04| **[72. Edit Distance](https://leetcode.com/problems/edit-distance/)** | [Python](https://tinyurl.com/wu6rdaw/72_Edit_Distance.py)| **[educative.com](https://tinyurl.com/wzxp6ef)**, **[algoexpert.io](https://tinyurl.com/szk8rub)**, **[codinginterviewclass.com](https://tinyurl.com/rj6d8fm)**, [Vid 1](https://tinyurl.com/y6chhmm9), [Vid 2](https://tinyurl.com/y4a7ohay)| Hard | TODO: Check again. Very important and classic. Levenshtein Distance |
|05| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)| [Python](https://tinyurl.com/wu6rdaw/70_Climbing_Stairs.py)| **[educative.io](https://tinyurl.com/rs9jfvd)** | Easy | Fibonacci sequence pattern |
|06| [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)| [Python](https://tinyurl.com/wu6rdaw/96_Unique_Binary_Search_Trees.py)| [educative.io](https://tinyurl.com/s9y9sya), [Vid 1](https://tinyurl.com/ut8wh4u), [Art 1](https://tinyurl.com/wuzpywc), [Vid 2](https://tinyurl.com/vb3s4jm), [Vis 3](https://tinyurl.com/uhet84g) | Medium | 📌 Fundamentals |
|07| [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)| [Python](https://tinyurl.com/wu6rdaw/95_Unique_Binary_Search_Trees_II.py)| [educative.io](https://tinyurl.com/s9y9sya) |  Medium | --- |
|08| [221. Maximal Square](https://leetcode.com/problems/maximal-square/)| [Python](https://tinyurl.com/wu6rdaw/221_Maximal_Square.py)| [Video 01](https://www.youtube.com/watch?v=_Lf1looyJMU), [Video 02](https://www.youtube.com/watch?v=FO7VXDfS8Gk)|
|09| [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)| [Python](https://tinyurl.com/wu6rdaw/85_Maximal_Rectangle.py)| [Video 01](https://www.youtube.com/watch?v=g8bSdXCG-lA)|
|10| [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)| [Python](https://tinyurl.com/wu6rdaw/42_Trapping_Rain_Water.py)| [Article 01](https://leetcode.com/problems/trapping-rain-water/solution/)| Hard | 📌 Check stack and 2 pointers based solutions |
|11| [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)| [Python](https://tinyurl.com/wu6rdaw/300_Longest_Increasing_Subsequence.py)| [educative.io](https://tinyurl.com/vcskq2n), [codinginterviewclass.com](https://tinyurl.com/yx477m32), [algoexpert.io](https://tinyurl.com/ydhxzrbb), [Vid 01](https://tinyurl.com/ufcrusx), [Vid 2](https://tinyurl.com/vldt7sd) | Medium | 📌 Need to check Binary Search approach, which is a lot harder |
|12| [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)| [Python](https://tinyurl.com/wu6rdaw/1143_Longest_Common_Subsequence.py)| [educative.io](https://tinyurl.com/qvv8dje), [algoexpert.io](https://tinyurl.com/vlkmx4c) | Medium | 📌 Classic DP |
|13| [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)| [Python](https://tinyurl.com/wu6rdaw/5_Longest_Palindromic_Substring.py)| [educative.io](https://tinyurl.com/rwouqnc), [algoexpert.io](https://tinyurl.com/rdaxfyc), [Vid 1](https://tinyurl.com/sd7me6k) | Medium | 📌 Classic DP |
|14| [1066. Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/)| [Python](https://tinyurl.com/wu6rdaw/1066_Campus_Bikes_II.py)|  | Medium |📌 TODO: Backtracking solution is getting TLE. Solve it and implement it with DP also |
|15| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)| [Python](https://tinyurl.com/wu6rdaw/121_Best_Time_to_Buy_and_Sell_Stock.py)| [Vid 1](https://codinginterviewclass.com/courses/coding-interview-class/lectures/12305111) | Easy | Fundamental |
|16| [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)| [Python](https://tinyurl.com/wu6rdaw/122_Best_Time_to_Buy_and_Sell_Stock_II.py)| [Video 01](https://www.youtube.com/watch?v=blUwDD6JYaE)| Easy | More like Greedy |
|17| [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)| [Python](https://tinyurl.com/wu6rdaw/123_Best_Time_to_Buy_and_Sell_Stock_III.py)| **[Vid 1](https://www.youtube.com/watch?v=oDhu5uGq_ic&t=2s), [Vid 2](https://www.youtube.com/watch?v=Pw6lrYANjz4)** | Hard | Fundamental |
|18| [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)| [Python](https://tinyurl.com/wu6rdaw/188_Best_Time_to_Buy_and_Sell_Stock_IV.py)| **[Vid 1](https://www.youtube.com/watch?v=oDhu5uGq_ic&t=2s), [Vid 2](https://www.youtube.com/watch?v=Pw6lrYANjz4)** | Hard | **Getting "Memory Limit Exceeded"** |
|19| **[309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)**| [Python](https://tinyurl.com/wu6rdaw/309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py)| **[Must](https://tinyurl.com/syuepe6)**, [Art0](https://tinyurl.com/vbzcm6z), [Art1](https://tinyurl.com/vtuga7r), **[Must 2](https://tinyurl.com/vgqsw89)** , [Art 2](https://tinyurl.com/y8uojzjl), [Art 3](https://tinyurl.com/ul95d62)  | Medium | Very tricky, must check again. Couldn't solve |
|20| [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)| [Python](https://tinyurl.com/wu6rdaw/714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee.py)| **[Must Read](https://tinyurl.com/y7eaa7vk)** , [Art 2](https://tinyurl.com/wzawybe) | Medium | More like Greedy, but DP |
|21| **[198. House Robber](https://leetcode.com/problems/house-robber/)**| [Python](https://tinyurl.com/wu6rdaw/198_House_Robber.py)| **[Must](https://tinyurl.com/vp9v27d)**, **[educative.io](https://tinyurl.com/srtvmra)** | Easy | A Gold Mine |
|22| [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)| [Python](https://tinyurl.com/wu6rdaw/213_House_Robber_II.py)| [Art 1](https://tinyurl.com/wwza8d5), [Art 2](https://tinyurl.com/qtqwcl4) | Medium | --- |
|23| [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)| [Python](https://tinyurl.com/wu6rdaw/337_House_Robber_III.py)| **[Art 1](https://tinyurl.com/yd8zjvvj)** | Medium | **[Another gold mine](https://tinyurl.com/yd8zjvvj)**, hidden greedy and DFS |
|24| **[416. Partition Equal Subset Sum](https://tinyurl.com/rmf5upz)** | [Python](https://tinyurl.com/wu6rdaw/416_Partition_Equal_Subset_Sum.py)| **[educative.io](https://tinyurl.com/wpxxyjy)**, [Art 1](https://tinyurl.com/we99l2n), [Vid 1](https://tinyurl.com/vvtavaw), [Vid 2](https://tinyurl.com/wabhu46), [Vid 3](https://tinyurl.com/sk89wa3), [Vid 4](https://tinyurl.com/z352yjj) | Medium | **0/1 Knapsack**, Very important |
|25| **[494. Target Sum](https://tinyurl.com/ro8wdkz)** | [Python](https://tinyurl.com/wu6rdaw/494_Target_Sum.py)| **[educative.io](https://tinyurl.com/wfhzh29)**, **[MUST MUST READ](https://tinyurl.com/vmmaxbe)** | Medium | **0/1 Knapsack**, Very important. TODO: Not  DOne. Check again |
|26| **[343. Integer Break](https://tinyurl.com/qsmmtc3)** | [Python](https://tinyurl.com/wu6rdaw/343_Integer_Break.py)| **[Art 1](https://tinyurl.com/wfhzh29)**, **[Art 2](https://tinyurl.com/t2rky7o)** | Medium | **Unbounded Knapsack**. TODO: Not Done. Check again |
|27| **[516. Longest Palindromic Subsequence](https://tinyurl.com/r7rege5)** | [Python](https://tinyurl.com/wu6rdaw/516_Longest_Palindromic_Subsequence.py)| **[educative.io](https://tinyurl.com/rvh2x2v)**, **[Vid 1](https://tinyurl.com/vjodfau)**, [Vid 2](https://tinyurl.com/uob2dhd) | Medium | --- |
|28| [647. Palindromic Substrings](https://tinyurl.com/qw3blls) | [Python](https://tinyurl.com/wu6rdaw/647_Palindromic_Substrings.py)| **[educative.io](https://tinyurl.com/wbc4eqb)** | Medium | --- |
|29| [680. Valid Palindrome II](https://tinyurl.com/rcdbykq) | [Python](https://tinyurl.com/wu6rdaw/680_Valid_Palindrome_II.py)| **[educative.io](https://tinyurl.com/vehzweg)**, [Art 1](https://tinyurl.com/twetoqk), [Art 2](https://tinyurl.com/wve6da4) | Medium | --- |
|30| [1312. Minimum Insertion Steps to Make a String Palindrome](https://tinyurl.com/rhzxwa6) | [Python](https://tinyurl.com/wu6rdaw/1312_Minimum_Insertion_Steps_to_Make_a_String_Palindrome.py)| **[educative.io](https://tinyurl.com/vehzweg)** | Hard | --- |
|31| **[132. Palindrome Partitioning II](https://tinyurl.com/t2rqddx)** | [Python](https://tinyurl.com/wu6rdaw/132_Palindrome_Partitioning_II.py)| **[educative.io](https://tinyurl.com/ruuewtc)**, [algoexpert.io](https://tinyurl.com/u4l4zdk), [Vid 1](https://tinyurl.com/rkq7lbu), [Vid 2](https://tinyurl.com/t9cgysf) | Hard | TODO: Check again. Very difficult and important |
|32| **[718. Maximum Length of Repeated Subarray](https://tinyurl.com/t5ykzen)** | [Python](https://tinyurl.com/wu6rdaw/718_Maximum_Length_of_Repeated_Subarray.py)| **[educative.io](https://tinyurl.com/teew37b)** | Medium | **Longest Common Substring** variation |
|33| [583. Delete Operation for Two Strings](https://tinyurl.com/wlzmbfn) | [Python](https://tinyurl.com/wu6rdaw/583_Delete_Operation_for_Two_Strings.py)| **[educative.io](https://tinyurl.com/wy357cz)** | Medium | --- |
|34| [1092. Shortest Common Supersequence](https://tinyurl.com/qlpc52j) | [Python](https://tinyurl.com/wu6rdaw/1092_Shortest_Common_Supersequence.py)| **[educative.io](https://tinyurl.com/qmro98q)**, [Art 1](https://tinyurl.com/t87jfgg) | Hard | TODO: Not Done |
|35| [115. Distinct Subsequences](https://tinyurl.com/gudjxts) | [Python](https://tinyurl.com/wu6rdaw/115_Distinct_Subsequences.py)| **[educative.io](https://tinyurl.com/yx6s5c4m)** | Hard | TODO: Check again |
|36| **[97. Interleaving String](https://tinyurl.com/qmp8yn5)** | [Python](https://tinyurl.com/wu6rdaw/97_Interleaving_String.py)| **[educative.io](https://tinyurl.com/uzbogsf)**, [Vid 1](https://tinyurl.com/wlmpvjo) | Hard | TODO: Check again. Very difficult and tricky to understand |
|37| [1048. Longest String Chain](https://tinyurl.com/uvb5v6s) | [Python](https://tinyurl.com/wu6rdaw/1048_Longest_String_Chain.py)| [Art 1](https://tinyurl.com/tcslm9l) | Medium | Modified LIS |
|38| **[801. Minimum Swaps To Make Sequences Increasing](https://tinyurl.com/rvtcyvb)** | [Python](https://tinyurl.com/wu6rdaw/801_Minimum_Swaps_To_Make_Sequences_Increasing.py)| [Art 1](https://tinyurl.com/tzx7wpv), [Art 2](https://tinyurl.com/ugybcmz) | Medium | TODO: Check again. Very analytical and tricky to come up with |
|39| **[279. Perfect Squares](https://tinyurl.com/jcjc6kf)** | [Python](https://tinyurl.com/wu6rdaw/279_Perfect_Squares.py)| **[Must](https://tinyurl.com/raomm4y)**, [Vid 1](https://tinyurl.com/rxpaqe8), [Vis 2](https://tinyurl.com/uevqohx) | Medium | TODO: Check again. Very Important. Very analytical and tricky to come up with |
|40| **[139. Word Break](https://tinyurl.com/yyyy9dqz)** | [Python](https://tinyurl.com/wu6rdaw/139_Word_Break.py)| **[Must](https://tinyurl.com/sdzmo32)**, [Vid 1](https://tinyurl.com/s4hvakw), [Vis 2](https://tinyurl.com/rjwjanc), [Vid 3](https://tinyurl.com/rdxmwwg) | Medium | TODO: Check again. Very Important. |
|41| **[62. Unique Paths](https://tinyurl.com/j8xmh7u)** | [Python](https://tinyurl.com/wu6rdaw/62_Unique_Paths.py), [Swift](https://tinyurl.com/wuja3c4/62_Unique_Paths.swift)| **[Vid 1](https://tinyurl.com/wp6vsqq)**, [Art 1](https://tinyurl.com/roammlg), [Art 2](https://tinyurl.com/tt5fpjk) | Medium | TODO: Check again |
|42| **[152. Maximum Product Subarray](https://tinyurl.com/rxbfx5k)** | [Python](https://tinyurl.com/wu6rdaw/152_Maximum_Product_Subarray.py), [Swift](https://tinyurl.com/wuja3c4/152_Maximum_Product_Subarray.swift)| **[Vid 1](https://tinyurl.com/t24rc22)**, [Art 1](https://tinyurl.com/uzdpw4k) | Medium | Kadane's algorithm on multiplication |
|43| **[64. Minimum Path Sum](https://tinyurl.com/ugnoql2)** | [Python](https://tinyurl.com/wu6rdaw/64_Minimum_Path_Sum.py), [Swift](https://tinyurl.com/wuja3c4/64_Minimum_Path_Sum.swift)| --- | Medium | --- |
|44| **[91. Decode Ways](https://tinyurl.com/t5yx86t)** | [Python](https://tinyurl.com/wu6rdaw/91_Decode_Ways.py), [Swift](https://tinyurl.com/wuja3c4/91_Decode_Ways.swift)| [Vid 1](https://tinyurl.com/wxc7jlj) | Medium | --- |
|45| **[975. Odd Even Jump](https://tinyurl.com/y5ovyklj)** | [Python](https://tinyurl.com/wu6rdaw/975_Odd_Even_Jump.py), [Swift](https://tinyurl.com/wuja3c4/975_Odd_Even_Jump.swift)| [Vid 1](https://tinyurl.com/vxyed3g), **[Art 1](https://tinyurl.com/wbjrnyt)** | Hard | DP using stack. Vary tricky and Interesting problem, loved it |
|46| **[562. Longest Line of Consecutive One in Matrix](https://tinyurl.com/u2fb4a6)** | [Python](https://tinyurl.com/wu6rdaw/562_Longest_Line_of_Consecutive_One_in_Matrix.py), [Swift](https://tinyurl.com/wuja3c4/562_Longest_Line_of_Consecutive_One_in_Matrix.swift)| [Art 1](https://tinyurl.com/vqppbae), [Art 2](https://tinyurl.com/t3xtfq8) | Medium |  |
|47| **[552. Student Attendance Record II](https://tinyurl.com/tnxj5oa)** | [Python](https://tinyurl.com/wu6rdaw/552_Student_Attendance_Record_II.py), [Swift](https://tinyurl.com/wuja3c4/552_Student_Attendance_Record_II.swift)| [Art 1](https://tinyurl.com/rdt2cgr), [Art 2](https://tinyurl.com/s8okmdb), [Art 3](https://tinyurl.com/uhggppt) | Hard | **This is a FUCKING difficult DP problem. Don't dare to solve it** |
|48| **[1320. Minimum Distance to Type a Word Using Two Fingers](https://tinyurl.com/ur876a6)** | [Python](https://tinyurl.com/wu6rdaw/1320_Minimum_Distance_to_Type_a_Word_Using_Two_Fingers.py), [Swift](https://tinyurl.com/wuja3c4/1320_Minimum_Distance_to_Type_a_Word_Using_Two_Fingers.swift)| [Vid 1](https://tinyurl.com/u5fcb3z), [Art 1](https://tinyurl.com/w386adm), [Art 2](https://tinyurl.com/rnkbhp3), [Art 3](https://tinyurl.com/tqwgraz), [Art 4](https://tinyurl.com/v46fuzm) | Hard | **Important. TODO: Check again** |
|49| **[688. Knight Probability in Chessboard](https://tinyurl.com/y8qgukyr)** | [Python](https://tinyurl.com/wu6rdaw/688_Knight_Probability_in_Chessboard.py), [Swift](https://tinyurl.com/wuja3c4/688_Knight_Probability_in_Chessboard.swift)| [Art 1](https://tinyurl.com/ycfu5ux4), [Art 2](https://tinyurl.com/y987zy5g), [Art 3](https://tinyurl.com/ybtv5p5m) | Medium(Really!) | **Important, and fucking difficult. TODO: Check again** |
|50| **[140. Word Break II](https://tinyurl.com/yb9yotou)** | [Python](https://tinyurl.com/wu6rdaw/140_Word_Break_II.py), [Swift](https://tinyurl.com/wuja3c4/140_Word_Break_II.swift)| [Art 1](https://tinyurl.com/yc9jvbpl), [Art 2](https://tinyurl.com/yaa7b7lu) | Hard | **OHH Boy, you must recheck this, Important. TODO: Check again.  An unique combination of DP, DFS and Backtracking** |
|51| **[1027. Longest Arithmetic Sequence](https://tinyurl.com/y7w7mmfn)** | [Python](https://tinyurl.com/wu6rdaw/1027_Longest_Arithmetic_Sequence.py), [Swift](https://tinyurl.com/wuja3c4/1027_Longest_Arithmetic_Sequence.swift)| [Art 1](https://tinyurl.com/ycto2x5o), [Art 2](https://tinyurl.com/yab7byj5) | Medium | **I didn't know that map can be used in 1d bottom-up dp. learned new things** |
|52| **[304. Range Sum Query 2D - Immutable](https://tinyurl.com/ybhblo57)** | [Python](https://tinyurl.com/wu6rdaw/304_Range_Sum_Query_2D_Immutable.py), [Swift](https://tinyurl.com/wuja3c4/304_Range_Sum_Query_2D_Immutable.swift)| [Art 1](https://tinyurl.com/ycto2x5o), [Art 2](https://tinyurl.com/yab7byj5) | Medium | **very good question, classical** |
|53| **[1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://tinyurl.com/ybte7ydl)** | [Python](https://tinyurl.com/wu6rdaw/1477_Find_Two_Non_overlapping_Sub_arrays_Each_With_Target_Sum.py), [Swift](https://tinyurl.com/wuja3c4/1477_Find_Two_Non_overlapping_Sub_arrays_Each_With_Target_Sum.swift)| [Art 1](https://tinyurl.com/y7rshs2j), [Art 2](https://tinyurl.com/y8x7cgxl) | Medium | **Very interesting and deceiving and tricky problem. An unique combination of sliding window and DP** |
|54| **[368. Largest Divisible Subset](https://tinyurl.com/ya8sv5jr)** | [Python](https://tinyurl.com/wu6rdaw/368_Largest_Divisible_Subset.py), [Swift](https://tinyurl.com/wuja3c4/368_Largest_Divisible_Subset.swift)| Official Solution | Medium | **Interesting problem.** |
|55| **[523. Continuous Subarray Sum](https://tinyurl.com/y6ce49ln)** | [Python](https://tinyurl.com/wu6rdaw/523_Continuous_Subarray_Sum.py), [Swift](https://tinyurl.com/wuja3c4/523_Continuous_Subarray_Sum.swift)| **[Art 1](https://tinyurl.com/yb3ya47s)** | Medium | **Tricky to see the DP** |
|56| **[689. Maximum Sum of 3 Non-Overlapping Subarrays](https://tinyurl.com/y9nlm8tg)** | [Python](https://tinyurl.com/wu6rdaw/689_Maximum_Sum_of_3_Non_Overlapping_Subarrays.py), [Swift](https://tinyurl.com/wuja3c4/689_Maximum_Sum_of_3_Non_Overlapping_Subarrays.swift)| **[Art 1](https://tinyurl.com/__)** | Hard | **Mainly, tricly array index manipulation. TODO: need to solve it in DP and sliding window approach** |
|57| **[338. Counting Bits](https://tinyurl.com/y5ly38nj)** | [Python](https://tinyurl.com/wu6rdaw/338_Counting_Bits.py), [Swift](https://tinyurl.com/wuja3c4/338_Counting_Bits.swift)|  | Medium | --- |
|58| **[1269. Number of Ways to Stay in the Same Place After Some Steps](https://tinyurl.com/y43jo8j3)** | [Python](https://tinyurl.com/wu6rdaw/1269_Number_of_Ways_to_Stay_in_the_Same_Place_After_Some_Steps.py), [Swift](https://tinyurl.com/wuja3c4/1269_Number_of_Ways_to_Stay_in_the_Same_Place_After_Some_Steps.swift)| [Art 1](https://tinyurl.com/yynv9xe2) | Hard | Loved the problem. Very versatile |
|59| **[1277. Count Square Submatrices with All Ones](https://tinyurl.com/y6a82a9r)** | [Python](https://tinyurl.com/wu6rdaw/1277_Count_Square_Submatrices_with_All_Ones.py), [Swift](https://tinyurl.com/wuja3c4/1277_Count_Square_Submatrices_with_All_Ones.swift)| [Must](https://tinyurl.com/y4sa8zgk) | Medium | --- |


</p>
</details>


- Signs:
  - Overlapping Subproblems 
  - Optimal Substructure (buying travel tickets)
- steps: 
  - write recursive
    - reduce args
  - draw recurse tree
    - det state
    - det old vs new state relation
  - write DP
    - inputs becomes axes (e.g 3 inputs => 3D DP)
1. **Fibonacci** - 1D: since only need prev val and prev-prev val, beginning always directly affects answer
  - Decode Ways 
  - Climbing Stairs
2. **0/1 Knapsack** - 2D: since need 2 types of vals: avail items and target val
  - Equal Subset Sum Partition
```python
def knapsack(vals, wts, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(vals) + 1)]
    for i in range(len(dp)):                #items
        for w in range(len(dp[0])):         #weights
            if i == 0 or w == 0:            #if you're not considering any items or you have 0 allowed wt
                dp[i][w] = 0
                                            # if curr item's wt is too large, we cant consider it for this curr wt
                                            # so just refer to val above ()
            elif wts[i - 1] > w:
                dp[i][w] = dp[i - 1][w]     # Up
            else:
                                            # max of: best val while not considering the curr item and 
                                            # val of curr item + best while not considering the curr item at the remaining weight
                                            # max(UpLeft, Up)
                dp[i][w] = max(vals[i-1] + dp[i - 1][w - wts[i - 1]], dp[i - 1][w])
    return dp[-1][-1]
```

3. **Boundless Knapsack** (can repeat items) 1D: since only need to know best val at lower weight
  - Coin Change
```python
def coinChange(self, coins: List[int], amount: int) -> int:
     max = float('inf')
                        # [0, inf, inf, inf...]
        dp = [0] + amount * [max]
                        # dont need to cover amount == 0 since we already have it in "dp"
                        # add 1 to iter up to amount
        for amt in range(1, amount + 1):
                        # add 1 since we're spending/using a coin now
                        # amt - coin can be == 0 since we need to hit 0..
                        #           use max if you would go below 0 (invalid coin option)
                        # Left
            dp[amt] = min([dp[amt - coin] if amt - coin >= 0 else max for coin in coins]) + 1
                        # 2 elem arr and we idx either at 0 or 1
                        # if dp.last == inf, True is 1 so then return -1
                        # if dp has a val, False is 0 so return that val
        print(dp)
        return [dp[amount], -1][dp[amount] == max]
```

4. **Longest Palindromic Subsequence** - 2D: 2 Pointers on 1 arr/str to delin a Window (Palindrome-specific)
```python
bbbab
12345
                    # 1 2 3 3 4 <-- res
                    # 0 1 2 2 3
                    # 0 0 1 1 3
                    # 0 0 0 1 1
                    # 0 0 0 0 1
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)] 
for i in range(n): #seed the cells where i == j
    dp[i][i] = 1
for cl in range(2,n+1):           # DIAGONAL traverse
    for i in range(n - cl + 1): # "nickel"
        j = i + cl - 1  # "icicle"
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2   #looks LD
        else:
            dp[i][j] = 
                                # logic for break in palindrome
                                # can resume by using other squares (if doing "subsequences", can use max(L, D, LD))
return dp[0][-1]                # return TopRight
```
5. **Longest Common Substring** - 2 Pointers (1 on each arr/str), beginning might not directly affect answer
  - Longest Common Subseq (LCS)
  - Shortest Common Superseq
```python
def LCS(text1, text2):
    m = len(text1)
    n = len(text2)  

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]   #0 buffer
    for i in range(1, len(dp)):                 
        for j in range(1, len(dp[0])):  
            if text1[i - 1] == text2[j - 1]:                # DP is 1-indexed
                dp[i][j] = dp[i - 1][j - 1] + 1             # LeftUp + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  #carry through max(Left, Up)
    return dp[-1][-1]        #BottomRight
```
  - Longest Increasing Subseq (LIS)
```python
def LIS(nums):
    if not nums: return 0
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:           #   if curr val > earlier val and it'd sets new best then look Left 
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp) 
```

- 2D array for X vs. Y "graph"
- Probability
- Memoizing: @functools.lru_cache(None)     (not dp, only similar)

### 2. Sorts and Searches
- Quick sort - worst case O(n^2)
- Merge sort - stable
- Insertion sort
- Radix sort
- Iterative B-search
```python
    lo, hi = 0, len() 
    while(lo < hi) {
        mid = lo + (hi - lo) / 2;
    if( #Special condition passed)(optional):
        return mid; 
    if( #condition passed)
    hi = mid;
    else 
    lo = mid + 1;
    }
    return lo;
```
- bisect.bisect(iterable, target) does BS but returns idx + 1 so do - 1 after
  - can also find where to insert a target
- Reservoir Sampling
- random.random()*3#1  (0, 1, 2)


- Binary Search
```python

def binarySearch(x, n):
  
  if x == 0:
    return 0
  
  lo, hi = 0, x
  diff = float('inf')
  
  while lo < hi :
    
    mid = float(hi + lo) / 2
    
    mid_n =  mid**n
    diff = x - mid_n
    
    if abs(diff) <= .001:
      return mid
    
    elif x > mid**n:
      lo = mid 
    
    elif x < mid**n :
      hi = mid 
    
  return -1

```

### 3. Graphs
- visited
  - separate 2D array 
  - visited = set() .add(str([xi, yj]))
- Tradeoffs
  - Adjacency matrix
  - graph
  - Class
- BFS, DFS
- Graph - BFS
  - don't use [-1] for ranges (will mess up when combined with dirs)
```python
visited = set()
dirs = []
for x, y in dirs:
    xi, yj
    if 0 <= xi < len and 0 <= yj < len
        if (xi, yj) not in visited:
```
```python
visited = set()
q = []
while q:
    q.pop
    visited.add
    for neighbor in .neighbors:
        if not in visited:
            q.append
```
```python

def shortestCellPath(grid, sr, sc, tr, tc):
  rows, cols = len(grid), len(grid[0])
  directions = ((-1,0),(1,0),(0,-1),(0,1))
  
  ans = float('inf')
  
  def dfs(r, c, visited, steps):
    if (r,c) == (tr,tc):
      return steps
      
    # validation
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited:
      return float('inf')
    visited.add((r,c))
    dfs(r+1, c, visited, steps+1)
    dfs(r-1, c, visited, steps+1)
    dfs(r, c+1, visited, steps+1)
    dfs(r, c-1, visited, steps+1)
  
  
  ans = min( ans, dfs(sr, sc, set(), 0))
  return ans if ans != float('inf') else -1


```


### 4. Trees
- acyclic graphs
- Traversals
  - inorder gives sorted
- DFS
```
.left
.right
```
- BFS
```python
q = []
newQ = []
newQ << .left
newQ << .right
```
- Level Order
- Tries
  - creating - #words * #avgLetters
  - searching - #letters
```python
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)   # makes itself {ref: TreeNode}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()  #abstracts away TrieNode
    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children[c]  #creates the child if not there
        root.isWord = True
    def search(self, word):
        root = self.root
        for c in word:
            root = root.children.get(c) #does not create
            if not root: return False
        return root.isWord
```

- Heaps
  - heapq
    - .heapify(<arr>)
    - .heappush(<heap>, el)
    - .heappop(<heap>)
  - sorts ASC by [0] so [0][0] is the smallest val it sees
  - insert and delete are O(logn)
  - creating a heap is NOT O(nlogn) even though it's n els * logn insert time...
    - time is amortized to **O(n)**
  - insert => sift up
  - remove min/max => swap then sift down

### 5. Strings and Arrays
- ord() and chr()
- Kadane’s - largest contig sum in subarr
- Two pointers
- Slow and Fast pointer
- satisfying additional subarrays: 
    res += count
    count += 1
- Moving Window
```python
counts = { } #usually a hash of element frequencies in window (collections.Counter)
currCount #some constraint on window
bestLength = 0
start = 0
for end in range(len(string)):
    currCount += function(input[end])               #el at end contributes to currCount

    if :                                #if window does not satisfy (e.g end - start - 1 > constraint or currCount > constraint):
        currCount -= function(input[start])                 #el at start is no longer being considered
        start += 1

    bestLength = max(bestLength, end - start + 1)           #update bestLength
      
return bestLength
```
- in-place:
  - make els - 

### 6. Intervals
- Inserting
  - map based on start, [0], sort, bisect.bisect(arr, newInterval[0]), then .insert
```python
    starts = [interval[0] for interval in intervals] 
    starts.sort()
    idx = bisect.bisect(starts, newInterval[0])
    intervals.insert(idx, newInterval)
```
- Merging
  - if [i][1] > [i + 1][0] then set [i][1] to max([i][1], [i + 1][1])
  if current's end is GREATER than next's start, then set currs end to the GREATER end
```python
    merged = [intervals[0]]        #seed it with the 1st interval
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]: #last el's end
            merged[-1][1] = max(merged[-1][1], intervals[i][1]) # absorb it
        else:
            merged.append(intervals[i])
    return merged
```
- isOverlap?
  - start1 < end2 and start2 > end1
- Overlap area
  - max(start1, start2) - min(end1, end2)
### 7. Pathing

- Dijkstra’s (2 dicts and 1 set)
  - finds shortest distance to every node
  - visit all nodes once
    - for each node, check dist for all neighbors
(source is “a”)
```python

        def findClosest(self, best, visited): #Find the closest (to orig src), unvisited node 
            res = None
            for node in best:
                if node not in visited and (not res or best[node] < best[res]):
                    res = node
            return res
                                                    # K = starting node, N = # of nodes
                                                    # all nodes receive signal
        graph = collections.defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]       #graph[src][dest] = edge
  
        best = dict()           # {a: 2, b: 3}
        for i in range(1, N + 1):
            best[i] = float('inf')
        best[K] = 0
        
        visited = set()
        
        for _ in range(N): 
            closest = self.findClosest(best, visited)
            visited.add(closest)
            for neighbor in graph[closest]:
                best[neighbor] = min(best[closest] + graph[closest][neighbor], best[neighbor])    # src to curr + curr to neigh

        for val in best.values():       #check if we can reach every other node
            if val == float('inf'): return -1
         
        return          #some value in best                      
```

### 8. Bit manipulation
- & | ~
- ^ 
  - finds rightmost 1
  - finds the one duplicate el
- << >>   multiply by 2
- change / check / clear a specific bit
  - shift a "1" over X times using <<
  - maybe ~ (not) it
  - & or | it with your number
- bin() to convert to bin OR
 - format(<num>, '#010b') to keep padding
- int(<binary string>, 2) to convert back to int

### 9. Other Data Structures / Algorithms
- Union Find (num of connected components)
  - keep finding a deeper root until the root matches the node
```python
# input: 
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]               # list of undirected edges
# n  = 5

# n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

roots = [i for i in range(n)]

def find(key):
    while key != roots[key]:
        key = roots[key]

for edge in edges:
    root1 = find(edge[0])
    root2 = find(edge[1])
    if root1 != root2:
        roots[root1] = root2
        #logic for being in same group ex: count -= 1
    else:
       #logic for being in diff group
```
- Topological Sort (alien dic)
  - for Directed Acyclic graphs
  - orders are not the only "right" answer
  - when you've explored all prereqs/predecessors, then add it to "order"
  - DFS method (recursive calls) or BFS (Queue)
  - need to sometimes check for cycles too
```python
    input:
    words = {"baa", "abcd", "abca", "cab", "cad"} #(given sorted)

    prereqs = {
        : []
    }

    order = []

    visited = {}

    def dfs(node):
        visited.add(node)
        for neigh in neighbor:
            if not in visited: dfs(neigh)
        order.append(node)

    for node in numNodes:
        if node not in visited:
            dfs(node)

    return order[::-1]

```

### 10. Backtracking
- can mutate outer res using 
  - [] assignment
  - .append
- can change curr using:
  - curr + [ ]
  - curr.append  curr.pop
- copy.deepcopy(arr) 
- Combinations / Permutations
  - list(itertools.combinations(arr, #)) [(), ()]
  - list(itertools.permutations(arr, #)) [(), ()]
```
res = []
def recurse(curr, idx)
    res.append(curr[::]) if
    for i in range(idx, len)
    .append
    recurse
    .pop
recurse([], 0)
```
- .isdigit  
- .isalpha
 
### 11. Linked Lists
- Strategies:
  - fast and slow - finds middle, start of cycle
    - Deleting -
    - Dummy node
- Reversing - 3 pointers
    - Null node
- Merging - 3 pointers
    - swap between lists
- triple swaps

```python
tail, head = l1, l1
l1 = l1.next            #l1 head already accounted for by tail
while l2:
    tail.next = l2
    l2 = l2.next
    tail = tail.next
    if l1:
        l1, l2 = l2, l1
return head
```

### 12. Stacks / Queues
- .deque 
- validParens
```python
count = 0
for char in s:
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1
        if count < 0: return False
return count == 0

```

### 13. Extra Knowledge
- Rabin Karp - hashing to find pattern in string
  - turn curr window into hash (integer. e.g 234)
  - convert when window slides (e.g. 345)
  - if currWindow hash == target hash, then compare actual chars
- Self-balancing Trees
  - AVL
  - Black Red Trees
- Sieve of Eratosthenes (finding every prime up to n)
  - check every number up to n 
  - eliminate every num starting at n^2 and incrementing by n
  - go to next unelimiminated 
- Bellman-Ford - one node to others
- Floyd-Warshall - short dist poss between all pairs of nodes
  - n^3
- Minimum Spanning Trees 
  - Kruskal - sort edges, keep adding smallest edge (not nec contiguous) that would connect trees
  - Prim - choose random node, keep choosing smallest accessible edge that would add an unvisited node


### Key Python methods
- list(string)      #how to split a word
- ternary
  - x = 1 if True else 2  #no colon
- [[for j in range] for i in range]
- array iterating backwards
  - [::][::-1]
  - dont use [-1:0:-1]  (starts at [-1], doesnt touch [0]) (awkward...)
- collections
  - Defaultdict		like Hash.new(0)
  - Deque
  - Counter.items()
- sorted(    .sort(key=
  - sorts by [0] by default for 2D arrs
  - ([0], [1]) *tuple* to sort by multiple fields
- reversed(    .reverse
- Find 	rfind()  	like indexOf
- Strings
  - lstrip rstrip
  - startswith() endswith()
- [list(row) for row in list(zip(*reversed(board)))]  starboard! (Python3 syntax)
  - need to convert zip object
- Arrays: 
  - any(el > 5 for el in arr)
  - all(el > 5 for el in arr)
    - len(set(a) == 1)  #checks if all the same val
  - del arr[] 
  - remove(val) 
  - insert(idx, val)
  - extend(arr2)
  - "map" == [x**2 for x in arr] 
    - map(lambda a: , <iter>)
  - "filter" == [x for x in arr if x > 2] 
    - filter(lambda a: <iter>)
  - "flatten" == [y for x in graph[x] for y in x]
- Sets:
  - can't hash lists / dicts (CAN hash objects)
  - declared with { }
  - set1.union(set2) |= 
  - set1.intersection(set2) &=
  - .add 
  - .discard/.remove to remove 
- range(start, end, step)
- sum(<2darray>, []) will flatten it
- isinstance(<item>, <type>)
 
- range is a lazy iterable like iterators but range is not an iterator
  - iterators

Suggestions:
LL => pointers
rotated / sorted => bSearch
logn time => bSearch / bTree
k branches at each level of recurs tree, n levels => k^n time
top k => min or max heap / quickselect
items in arr/str interacting => stack
rectangle/meeting time/free time => interval
anagram => hash
subsequence => dp
prereqs => topo sort

Time complexities:
Trees: 
    (n^2) to make BST (worst case)
    (nlogn) to make AVL
    (n) to make Heap
    => heap is only way to improve time complex
    finding kth smallest => klogn for minHeap / (n-k)logk time
    O(n) to traverse tree   
    
    Search, insert, delete
    Binary Tree
        O(n)
    BST
        O(n) but technically, O(h) 
    AVL
        O(logn)
    when to make a tree:
        sorted array - O(n) insert. would need to reallocate (re-size)
        linked list - O(n) search


