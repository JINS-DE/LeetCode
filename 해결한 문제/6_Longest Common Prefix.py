class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare_word=strs[0]
        for w in strs[1:]:
            tmp=""
            for c in range(min(len(w),len(compare_word))):
                if compare_word[c] == w[c] :
                    tmp+=w[c]
                else:
                    break
            compare_word = tmp
        return compare_word

# # gpt
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         # 첫 번째 문자열을 기준으로
#         prefix = strs[0]

#         for s in strs[1:]:  # 두 번째 문자열부터 비교
#             while not s.startswith(prefix):  # 현재 prefix로 시작하지 않으면 줄임
#                 prefix = prefix[:-1]  # 맨 끝 문자를 제거
#                 if not prefix:  # prefix가 빈 문자열이 되면 중지
#                     return ""

#         return prefix


print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"