from functools import lru_cache

@lru_cache(maxsize=None)
def count(p, s, h=0):
    if not p:
        return not s and not h
    n = 0
    if p[0] in "#?":
        n += count(p[1:], s, h + 1)
    if p[0] in ".?" and (s and s[0] == h or not h):
        n += count(p[1:], s[1:] if h else s)
    return n


with open("day12_input") as f:
    ls = [l.split() for l in f.read().splitlines()]
ls = [(p, tuple(int(n) for n in s.split(","))) for p, s in ls]

#print(sum(count(p + ".", s, 0) for p, s in ls))
print(sum(count("?".join([p] * 5) + ".", s * 5) for p, s in ls))
