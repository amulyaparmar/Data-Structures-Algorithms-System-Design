def A_n_k(a, n, k, depth, used, curr, ans):
  '''
  Implement permutation of k items out  of n items
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  curr: the current partial solution
  ans: collect all the valide solutions
  '''
  if depth == k: #end condition
    ans.append(curr[::]) # use deepcopy because curr is tracking all partial solution, it eventually become []
    return
  
  for i in range(n):
    if not used[i]:
      # generate the next solution from curr
      curr.append(a[i])
      used[i] = True
      print(curr)
      # move to the next solution
      A_n_k(a, n, k, depth+1, used, curr, ans)
      
      #backtrack to previous partial state
      curr.pop()
      print('backtrack: ', curr)
      used[i] = False
  return

# [1]
# [1, 2]
# [1, 2, 3]             <--------
# backtrack:  [1, 2]
# backtrack:  [1]
# [1, 3]
# [1, 3, 2]             <--------
# backtrack:  [1, 3]
# backtrack:  [1]
# backtrack:  []
# [2]
# [2, 1]
# [2, 1, 3]             <--------
# backtrack:  [2, 1]
# backtrack:  [2]
# [2, 3]
# [2, 3, 1]             <--------
# backtrack:  [2, 3]
# backtrack:  [2]
# backtrack:  []
# [3]
# [3, 1]
# [3, 1, 2]             <--------
# backtrack:  [3, 1]
# backtrack:  [3]
# [3, 2]
# [3, 2, 1]             <--------
# backtrack:  [3, 2]
# backtrack:  [3]
# backtrack:  []