def DC(label, operand):
    return f"<{label}><-{operand}"

def DS(label, operand):
    return f"allocate {operand} words for {label}"    

def LD(opr):
    args = opr.split(',')
    if len(args) == 2:
        r, adr = args
        return f"{r}<-({adr})"
    else:
        r, adr, x = args
        return f"{r} <- ({adr} + {x})"

def LAD(opr):
    args = opr.split(',')
    if len(args) == 2:
        r, adr = args
        return f"{r}<-{adr}"
    else:
        r, adr, x = args
        return f"{r} <- {adr} + {x}"

def SUBA(opr):
    r1, r2 = opr.split(',')
    return f"{r1} = {r1} - {r2}"

def CPA(opr):
    r1, r2 = opr.split(',')
    return f"{r1}:{r2}"

def JMI(opr):
    return f"SF=1 then goto {opr}"

def JUMP(opr):
    return f"goto {opr}"

def ST(opr):
    args = opr.split(',')
    
    if len(args) == 2:
        r, adr = args
        return f"<{adr}><-{r}"
    else:
        r,adr,x = args
        return f"<{adr}+{x}<-{r}"


COMMENT_RULES = {
    "DC": DC,
    "DS": DS,
    "LD": LD,
    "LAD": LAD,
    "SUBA": SUBA,
    "CPA": CPA,
    "JMI": JMI,
    "JUMP": JUMP,
    "ST": ST,
}


def add_comment(line):
    if line.strip() == "" or line.lstrip().startswith(";"):
        return line

    parts = line.rstrip().split('\t')

    label = ""
    opcode = ""
    operand = ""

    if len(parts) == 3:
        label, opcode, operand = parts
    elif len(parts) == 2:
        opcode, operand = parts
    else:
        return line

    opcode = opcode.upper()

    if opcode not in COMMENT_RULES:
        return line

    if opcode == "DC" or opcode == "DS":
        comment = COMMENT_RULES[opcode](label, operand)
    else:
        comment = COMMENT_RULES[opcode](operand)

    return f"{line.rstrip()}\t;{comment}"


def main():
    filename = input("ファイルのディレクトリを入力してください: ")

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    out = [add_comment(line) for line in lines]

    with open("output.cas", "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()