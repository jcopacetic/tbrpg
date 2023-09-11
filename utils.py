from enum import Enum

Types = Enum("Types", "normal, fire, water, ground, electricity")


def type_damage(type_1, type_2):
    damage_multipliers = {
        ('fire', 'water'): (0.9, 1.5),
        ('water', 'electricity'): (0.9, 1.5),
        ('electricity', 'ground'): (0.9, 1.5),
        ('water', 'fire'): (0.4, 0.8),
        ('electricity', 'water'): (0.4, 0.8),
        ('ground', 'electricity'): (0.4, 0.8),
    }

    min_p, max_p = damage_multipliers.get((type_1, type_2), (0.8, 1.2))

    return {
        "min_percent": min_p,
        "max_percent": max_p,
    }