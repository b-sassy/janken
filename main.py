import random
from enum import Enum


class JankenHand(Enum):
    "ジャンケンの手"
    グー = 0
    チョキ = 1
    パー = 2


def main():

    janken_dict = {"グー": JankenHand.グー, "チョキ": JankenHand.チョキ, "パー": JankenHand.パー}  # それぞれの手に対応する数字を設定する。
    print("じゃんけんポイ！")
    while True:  # あいこの場合に繰り返す条件を付与（あいこ以外はbreak）
        print("(グー、チョキ、パーのいずれかを入力してください。)")
        user_hand = JankenHand(janken_dict[input("あなたの手 -> ")])
        opponent_hand = JankenHand(random.randint(0, 2))  # 0~2の数値をランダムに生成する。
        try:
            # 下記以降の処理は、それぞれの手に応じた勝ち負けを出力させる。
            if (user_hand.value - opponent_hand.value) % 3 == 2:  # 自分の手 - 相手の手を3で割ったあまりが2の場合は自分の勝ち
                print(f"相手の手 -> {opponent_hand.name}")
                print("結果：あなたの勝ち")
                break

            if (user_hand.value - opponent_hand.value) % 3 == 1:  # 自分の手 - 相手の手を3で割ったあまりが1の場合は自分の負け
                print(f"相手の手 -> {opponent_hand.name}")
                print("結果：あなたの負け")
                
                break
            
            # 作成した辞書のキーに対応するバリューとランダムで生成された値が同じ場合は、あいこ
            print(f"相手の手 -> {opponent_hand.name}")
            print("結果：引き分け")
            print("=============")
            print("あいこでしょ！")

        except Exception:  # 指定した入力（今回の場合は、グー、チョキ、パーのいずれか）以外だとエラーが起きるので、その場合の処理
            print("=============")
            print("下記の入力を守ってください。")


if __name__ == '__main__':
    main()