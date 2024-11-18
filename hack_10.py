"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    name = "fooziman"

    change = name.replace("o","0").replace("i","1").replace("a","@").upper()
    new_result = list(change)
    return new_result