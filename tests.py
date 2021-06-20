import pytest

import member_mgmt

def test_ismember_1():
    assert member_mgmt.is_member(7, member_mgmt.Member.ADMIN) == False


def test_ismember_2():
    assert member_mgmt.is_member(2, member_mgmt.Member.STUDENT) == False


def test_ismember_3():
    assert member_mgmt.is_member(5, member_mgmt.Member.PRINCIPAL) == True


def test_getmember_1():
    assert member_mgmt.get_member(6) == 'директор, преподаватель'


def test_getmember_2():
    assert member_mgmt.get_member(8) == 'администратор'


def test_getmember_3():
    assert member_mgmt.get_member(15) == 'администратор, директор, преподаватель, ученик'

