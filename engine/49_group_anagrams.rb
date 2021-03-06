# Group Anagrams
# Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# * All inputs will be in lowercase.
# * The order of your output does not matter.

# create a hash
# iter over the input words
# iter the keys in the hash
# add it to the key's [] if its a permut
# if its not a permutation of anything, then create a new key for it

def group_anagrams(strs)
    hash = Hash.new {|h, k| h[k] = []}
    strs.map!.with_index{|str, idx| [str, str.split("").sort.join]}
    strs.each {|group|
        hash[group[1]] << group[0]
    }
    hash.values
end

print group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])