def solution(s, skip, index):
    result = ""
    for c in s:
        if c not in skip:
            # ord('a')는 97, ord('z')는 122입니다.
            # 알파벳의 범위를 벗어나면 다시 a부터 시작합니다.
            new_ord = ord(c) + index
            if new_ord > 122:
                new_ord -= 26
            new_c = chr(new_ord)
            while new_c in skip:
                # skip 문자열에 해당하는 알파벳은 건너뜁니다.
                new_ord += index
                if new_ord > 122:
                    new_ord -= 26
                new_c = chr(new_ord)
            result += new_c
    return result