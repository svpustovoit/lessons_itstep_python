'''
def black_hole(*args):
    print(f"args = {args},\n\t type(args) = {type(args)})")
    for argument in args:
        print(f"{argument} --> {type(argument)}")


black_hole(0, 4, 6, "25", "name", 2*5, [0, 24])

arg = 0, 4, 6, "25", "name", 2*5, [0, 24]
print(f"arg = {type(arg)}")

print()

def black_hole_named(**kwargs):
    print(f"kwargs = {kwargs},\n\t type(kwargs) = {type(kwargs)})")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_named(name="Nick", planet="Earth", school=217, lst=[2, "0"])

kw_arg = {'name': "Nick", 'planet': "Earth", 'school': 217, 'lst': [2, "0"]}
print(f"kw_arg = {kw_arg}, \n\ttype(kw_arg) - {type(kw_arg)}")

def black_hole_full(*args, **kwargs):
    print(f"args - {args}")
    print(f"kwargs - {kwargs}")
    for arg in args:
        print(f"arg - {arg}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_full(12, 45, ["a", 25], name="Nick", planet="Earth", school=217)


def black_hole_mixed(var_1, var_2=5, *args, **kwargs):
    print(f"var_1 = {var_1}")
    print(f"var_2 = {var_2}")
    for arg in args:
        print(f"arg - {arg}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")


black_hole_mixed(0.5, name="Nick", planet="Earth", school=217)
black_hole_mixed(0.5, 12, 12, 'strings', 2*5,
                 name="Nick", planet="Earth", school=217)



lst = [3, 60]   # v, a, t --> s = v*t=60*3=180    (км/ч) * ч = (км * ч) / ч = км
tpl = (60, 3)
dct = {"t": 3, "v": 60}

def way(v, t):
    print(f"S = {v} * {t} = {v * t}")

way(*lst)
way(*tpl)
way(**dct)
'''

# f-strings f-рядки






















