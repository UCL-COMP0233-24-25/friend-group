"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here..

# Jill，26岁，生物学家，是Zalika的朋友和John的伴侣
jill = {
    'name': 'Jill',
    'age': 26,
    'job': 'biologist',
    'connections': {
        'Zalika': 'friend',
        'John': 'partner'
    }
}

# Zalika，28岁，艺术家，Jill的朋友
zalika = {
    'name': 'Zalika',
    'age': 28,
    'job': 'artist',
    'connections': {
        'Jill': 'friend'
    }
}

# John，27岁，作家，Jill的伴侣
john = {
    'name': 'John',
    'age': 27,
    'job': 'writer',
    'connections': {
        'Jill': 'partner',
        'Nash': 'cousin'
    }
}

# Nash，34岁，厨师，John的表亲和Zalika的房东
nash = {
    'name': 'Nash',
    'age': 34,
    'job': 'chef',
    'connections': {
        'John': 'cousin',
        'Zalika': 'landlord'
    }
}

# 示例：没有工作和关系的人
alex = {
    'name': 'Alex',
    'age': 22,
    'job': None,
    'connections': {}
}

# 将所有人物加入列表
my_group = [jill, zalika, john, nash, alex]
