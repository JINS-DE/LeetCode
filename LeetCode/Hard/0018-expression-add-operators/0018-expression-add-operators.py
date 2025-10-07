"""
dfs를 통해 해결
- 재귀 종료 조건 (Base Case) 
    - if index == len(num)
    -   if current_eval == target : path를 정답에 추가

- validation 체크해야할 것 ("05"와 같은 0으로 시작하는 애들)
    - 0으로 시작하는 "05", "051"과 같은 잘못된 형태의 숫자로 계산되는 것의 뒤의 계산은 볼 필요도 없으니 break

- dfs 구성 요소 
    - index : 이후 계산해야할 시작 index
    - path : 지금까지 경로
    - current_eval : 지금까지 계산된 값
    - last_operand : 가장 최근에 연산된 값
"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        output=[]
        def dfs(index, path, current_eval, last_operand):
            if index==len(num):
                if current_eval==target:
                    output.append(path)
                return
            
            for j in range(index,len(num)):
                operanded_str = num[index:j+1]
                if len(operanded_str) > 1 and operanded_str[0]=='0':
                    break
                operanded_int = int(operanded_str)

                dfs(j+1, path + "+" + operanded_str, current_eval + operanded_int, operanded_int)
                dfs(j+1, path + "-" + operanded_str, current_eval - operanded_int, -operanded_int)
                dfs(j+1, path + "*" + operanded_str, (current_eval - last_operand)+last_operand*operanded_int, last_operand*operanded_int)
        
        # 첫 시작 어떤 숫자로 해줄지 
        for i in range(len(num)):
            first_str = num[:i+1]
            if len(first_str)>1 and first_str[0]=='0':
                break
            first_int = int(first_str)
            dfs(i+1,first_str,first_int,first_int)

        return output