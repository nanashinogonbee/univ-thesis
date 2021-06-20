from enum import Enum


class Member(Enum):
    ADMIN = 8
    PRINCIPAL = 4
    TEACHER = 2
    STUDENT = 1

def is_member(flags, group):
    return bool(flags & group.value)


def get_member(flags):
    roles = ('ученик', 'преподаватель', 'директор', 'администратор')
    result = [roles[i] for i in range(len(Member)) if flags & (2 ** i)]
    return ', '.join(result[::-1])


