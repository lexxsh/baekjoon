def solution(arr, commands):
    ans = []
    for command in commands:
        new = arr[command[0]-1:command[1]]
        new = sorted(new)
        ans.append(new[command[2]-1])
    return ans