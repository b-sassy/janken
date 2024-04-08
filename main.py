import random

def main():

    janken_dict = {"グー": 0, "チョキ": 1, "パー": 2} #それぞれの手に対応する数字を設定する。
    print("じゃんけんポイ！")
    while True: #あいこの場合に繰り返す条件を付与（あいこ以外はbreak）
        print("(グー、チョキ、パーのいずれかを入力してください。)")
        user_hand = input("あなたの手 -> ")
        opponent_hand = (random.randint(0, 2)) #0~2の数値をランダムに生成する。
        try:
            if janken_dict[user_hand] == opponent_hand: #作成した辞書のキーに対応するバリューとランダムで生成された値が同じ場合は、あいこ
                if opponent_hand == 0:
                    print("相手の手 -> グー")
                    print("結果：引き分け")
                    print("=============")
                    print("あいこでしょ！")

                elif opponent_hand == 1:
                    print("相手の手 -> チョキ")
                    print("結果：引き分け")
                    print("=============")
                    print("あいこでしょ！")

                elif opponent_hand == 2:
                    print("相手の手 -> パー")
                    print("結果：引き分け")
                    print("=============")
                    print("あいこでしょ！")
            #下記以降の処理は、それぞれの手に応じた勝ち負けを出力させる。
            elif janken_dict[user_hand] == 0 and opponent_hand == 1: #グー対チョキ
                print("相手の手 -> チョキ")
                print("結果：あなたの勝ち")
                break

            elif janken_dict[user_hand] == 0 and opponent_hand == 2: #グー対パー
                print("相手の手 -> パー")
                print("結果：あなたの負け")
                break

            elif janken_dict[user_hand] == 1 and opponent_hand == 0: #チョキ対グー
                print("相手の手 -> グー")
                print("結果：あなたの負け")
                break

            elif janken_dict[user_hand] == 1 and opponent_hand == 2: #チョキ対パー
                print("相手の手 -> パー")
                print("結果：あなたの勝ち")
                break

            elif janken_dict[user_hand] == 2 and opponent_hand == 0: #パー対グー
                print("相手の手 -> グー")
                print("結果：あなたの勝ち")
                break

            elif janken_dict[user_hand] == 2 and opponent_hand == 1: #パー対チョキ
                print("相手の手 -> チョキ")
                print("結果：あなたの負け")
                break

        except Exception: #指定した入力（今回の場合は、グー、チョキ、パーのいずれか）以外だとエラーが起きるので、その場合の処理
            print("=============")
            print("下記の入力を守ってください。")

if __name__ == '__main__':
    main()