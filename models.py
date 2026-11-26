# -*- coding: utf-8 -*-
"""ジム管理アプリ：会員と運動記録の共通データ定義。"""


class Member:
    def __init__(self, member_id, name="", address="", birth_date="",
                 height_cm=0.0, weight_kg=0.0):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.birth_date = birth_date
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class WorkoutRecord:
    def __init__(self, record_id, member_id, workout_date, exercise,
                 duration_minutes):
        self.record_id = record_id
        self.member_id = member_id
        self.workout_date = workout_date
        self.exercise = exercise
        self.duration_minutes = duration_minutes
