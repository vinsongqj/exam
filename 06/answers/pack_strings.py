def pack(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)


def unpack(s: str) -> list[str]:
    if not s:
        return []

    res = []
    i = 0
    n = len(s)

    while i < n:
        j = s.index('#', i)
        length = int(s[i:j])
        i = j + 1
        res.append(s[i:i + length])
        i += length

    return res
