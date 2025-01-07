''' 🚀 0ms | Beats 100% | Keep it simple silly python solution 😋
Python3
🧠Intuition
Use set to avoid duplicates

➡️Approach
A nested loop is used to compare each word in the list (words[i]) with every other word in the list (words[j]).

Outer Loop (for i in range(n):): Iterates through each word in the list as the "current word" (words[i]).

Inner Loop (for j in range(n):): Iterates through all words in the list as potential "containing words" (words[j]).

The condition i != j ensures that a word is not compared with itself.

The condition words[i] in words[j] checks if the current word (words[i]) is a substring of another word (words[j]).

If words[i] is a substring of words[j], it is added to the output set using output.add(words[i]).

The break statement exits the inner loop early once the word is found in another word. This prevents redundant checks.

Complexity
Time complexity: O(N^2) because of 2 loops
Space complexity: O(N) because of using set '''
#Code
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        output = set()
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    output.add(words[i])
                    break
        return list(output)
