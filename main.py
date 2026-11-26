# -*- coding: utf-8 -*-
"""ジム会員・ワークアウト管理（授業内実技課題用）。

起動方法：python main.py  または  py main.py
保存先はメモリです。再起動すると初期データに戻ります。
"""

from datetime import date
from models import Member, WorkoutRecord
from member import p07, p08, p09
from workout import add_workout, display_workout_history, calculate_total_minutes


def make_sample_data():
    members = [
        Member("M1001", "山田花子", "八王子市明神町", "1998-04-18", 163.0, 54.0),
        Member("M1002", "佐藤健太", "立川市曙町", "2001-09-12", 175.0, 68.0),
        Member("M1003", "鈴木直美", "日野市多摩平", "1994-02-25", 158.0, 51.0),
    ]
    records = [
        WorkoutRecord("W001", "M1001", "2026-11-05", "ウォーキング", 30),
        WorkoutRecord("W002", "M1002", "2026-11-10", "ランニング", 40),
        WorkoutRecord("W003", "M1002", "2026-11-11", "ヨガ", 20),
        WorkoutRecord("W004", "M1001", "2026-11-12", "筋トレ", 45),
        WorkoutRecord("W005", "M1003", "2026-11-13", "ランニング", 25),
        WorkoutRecord("W006", "M1001", "2026-11-14", "ランニング", 15),
    ]
    return members, records


def choose_member(members):
    member_id = input("会員ID（例：M1001）：").strip().upper()
    member = p07(members, member_id)
    if member is None:
        print("会員が見つかりません。")
    return member


def show_member_list(members):
    print("\n【登録済み会員】")
    for member in members:
        print(f"{member.member_id} | {member.name}")


def register_member(members):
    print("\n【新規会員登録】")
    print("※会員IDは自動発行されます。")
    name = input("氏名：")
    address = input("住所：")
    birth_date = input("生年月日（YYYY-MM-DD）：").strip()
    try:
        height_cm = float(input("身長（cm）："))
        weight_kg = float(input("体重（kg）："))
    except ValueError:
        print("身長・体重には数値を入力してください。")
        return

    member = p08(members, name, address, birth_date, height_cm, weight_kg)
    if member is None:
        print("入力内容を確認してください。登録は行われませんでした。")
        return
    print("登録しました。")
    p09(member)


def add_workout_from_menu(members, records):
    print("\n【ワークアウト記録の追加】")
    member = choose_member(members)
    if member is None:
        return
    workout_date = input("日付（YYYY-MM-DD）：").strip()
    try:
        date.fromisoformat(workout_date)
    except ValueError:
        print("日付の形式が正しくありません。")
        return
    exercise = input("種目：").strip()
    if not exercise:
        print("種目を入力してください。")
        return
    try:
        duration_minutes = int(input("運動時間（分）："))
    except ValueError:
        print("運動時間には整数を入力してください。")
        return
    if duration_minutes <= 0:
        print("運動時間は1分以上にしてください。")
        return
    record = add_workout(
        records, member.member_id, workout_date, exercise, duration_minutes
    )
    print(f"記録しました（記録ID：{record.record_id}）。")


def main():
    members, records = make_sample_data()
    print("=== ジム会員・ワークアウト管理システム ===")
    print("初期データ：会員3名、運動記録6件")
    print("※データは終了時に保存されません。")

    while True:
        print("\n--- メニュー ---")
        print("1：会員一覧")
        print("2：新規会員登録")
        print("3：会員検索")
        print("4：指定会員のワークアウト履歴")
        print("5：ワークアウト記録の追加")
        print("6：指定会員の累計運動時間")
        print("0：終了")
        choice = input("番号：").strip()

        if choice == "1":
            show_member_list(members)
        elif choice == "2":
            register_member(members)
        elif choice == "3":
            member = choose_member(members)
            if member is not None:
                p09(member)
        elif choice == "4":
            member = choose_member(members)
            if member is not None:
                print(f"\n【{member.name}さんの運動履歴】")
                display_workout_history(records, member.member_id)
        elif choice == "5":
            add_workout_from_menu(members, records)
        elif choice == "6":
            member = choose_member(members)
            if member is not None:
                minutes = calculate_total_minutes(records, member.member_id)
                print(f"累計運動時間：{minutes}分")
        elif choice == "0":
            print("終了します。")
            break
        else:
            print("メニュー番号を選択してください。")


if __name__ == "__main__":
    main()
