# -*- coding: utf-8 -*-
"""ワークアウト記録の登録、検索、集計。"""

from models import WorkoutRecord


def generate_record_id(records):
    """次の記録IDを作る。"""
    max_number = 0
    for record in records:
        number = int(record.record_id[1:])
        if number > max_number:
            max_number = number
    return f"W{max_number + 1:03d}"


def add_workout(records, member_id, workout_date, exercise, duration_minutes):
    """会員のワークアウト記録を追加する。"""
    new_record = WorkoutRecord(
        generate_record_id(records),
        member_id,
        workout_date,
        exercise,
        duration_minutes,
    )
    records.append(new_record)
    return new_record


def get_workout_history(records, member_id):
    """指定した会員の運動履歴を日付順に取得する。"""
    history = []
    for record in records:
        if record.member_id == member_id:
            history.append(record)
    return sorted(history, key=lambda record: (record.workout_date, record.record_id))


def calculate_total_minutes(records, member_id):
    """指定した会員の累計運動時間（分）を返す。"""
    total_minutes = 0
    for record in get_workout_history(records, member_id):
        total_minutes += record.duration_minutes
    return total_minutes


def display_workout_history(records, member_id):
    """指定会員の履歴を表示する。"""
    history = get_workout_history(records, member_id)
    if not history:
        print("該当する記録はありません。")
        return
    for record in history:
        print(
            f"{record.record_id} | {record.workout_date} | "
            f"{record.exercise} | {record.duration_minutes}分 "
            f"| 会員ID:{record.member_id}"
        )
