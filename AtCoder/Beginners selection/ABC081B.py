def is_valid(s):
    # 先頭と末尾の文字が異なる場合のみ True を返す
    return (s[0] == 'o' and s[-1] == '-') or (s[0] == '-' and s[-1] == 'o')

def max_level(s):
    # Xの値を1からNまで順に調べる
    for i in range(len(s)):
        # 長さi+1の部分文字列を順に調べ、レベルi+1のダンゴ文字列があるかどうかをチェックする
        for j in range(len(s) - i):
            if is_valid(s[j:j+i+2]):
                # ダンゴ文字列が見つかった場合、次に大きな値を探すためにXの値を1増やす
                level = i + 1
        else:
            # ダンゴ文字列が見つからなかった場合、ループを続ける
            continue
        # ダンゴ文字列が見つかった場合、次に大きな値を探すためにXの値を1増やす
        return level
    # ダンゴ文字列が見つからなかった場合は-1を返す
    return -1
