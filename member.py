# -*- coding: utf-8 -*-
"""会員管理処理。"""

from datetime import date
from models import Member


def p01(a):
    n = 1000
    for x in a:
        v = int(x.member_id[1:])
        if v > n:
            n = v
    return f"M{n + 1:04d}"


def p02(a, b):
    if not b.strip():
        return False
    a.name = b.strip()
    return True


def p03(a, b):
    if not b.strip():
        return False
    a.address = b.strip()
    return True


def p04(a, b):
    try:
        date.fromisoformat(b)
    except ValueError:
        return False
    a.birth_date = b
    return True


def p05(a, b):
    if not 0 < b <= 250:
        return False
    a.height_cm = b
    return True


def p06(a, b):
    if not 0 < b <= 300:
        return False
    a.weight_kg = b
    return True


def p07(a, b):
    for x in a:
        if x.member_id == b:
            return x
    return None


def p08(a, b, c, d, e, f):
    x = Member(p01(a))
    if not p02(x, b):
        return None
    if not p03(x, c):
        return None
    if not p04(x, d):
        return None
    if not p05(x, e):
        return None
    if not p06(x, f):
        return None
    a.append(x)
    return x


def p09(a):
    print(f"会員ID   : {a.member_id}")
    print(f"氏名     : {a.name}")
    print(f"住所     : {a.address}")
    print(f"生年月日 : {a.birth_date}")
    print(f"身長     : {a.height_cm:.1f} cm")
    print(f"体重     : {a.weight_kg:.1f} kg")
