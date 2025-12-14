# 2個目のオペランドがGRかどうか判定
def isGR(args):
    return args[1].startswith("GR")

#定義系
def DC(label, operand):
    return f"<{label}><-{operand}"

def DS(label, operand):
    word = "word" if operand == 1 else "words"
    return f"allocate {operand} {word} for {label}"

#読み書き系
def LD(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r2}"
        else:
            r, adr = args
            return f"{r}<-({adr})"
    else:
        r, adr, x = args
        return f"{r} <- ({adr}+{x})"

def LAD(opr):
    args = opr.split(',')
    if len(args) == 2:
        r, adr = args
        return f"{r}<-{adr}"
    else:
        r, adr, x = args
        return f"{r} <- {adr}+{x}"
    
def ST(opr):
    args = opr.split(',')   
    if len(args) == 2:
        r, adr = args
        return f"<{adr}><-{r}"
    else:
        r,adr,x = args
        return f"<{adr}+{x}><-{r}"

#演算系
def ADD(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r1}+{r2}"
        else:
            r, adr = args
            return f"{r}<-{r}+({adr})"
    else:
        r, adr, x = args
        return f"{r}<-{r}+({adr}+{x})"

def SUB(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r1}-{r2}"
        else:
            r, adr = args
            return f"{r}<-{r}-({adr})"
    else:
        r, adr, x = args
        return f"{r}<-{r}-({adr}+{x})"
    
def AND(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r1} AND {r2}"
        else:
            r, adr = args
            return f"{r}<-{r} AND ({adr})"
    else:
        r, adr, x = args
        return f"{r}<-{r} AND ({adr}+{x})"
    
def OR(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r1} OR {r2}"
        else:
            r, adr = args
            return f"{r}<-{r} OR ({adr})"
    else:
        r, adr, x = args
        return f"{r}<-{r} OR ({adr}+{x})"
    
def XOR(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}<-{r1} XOR {r2}"
        else:
            r, adr = args
            return f"{r}<-{r} XOR ({adr})"
    else:
        r, adr, x = args
        return f"{r}<-{r} XOR ({adr}+{x})"

# 比較
def CP(opr):
    args = opr.split(',')
    if len(args) == 2:
        if isGR(args):
            r1, r2 = args
            return f"{r1}:{r2}"
        else:
            r, adr = args
            return f"{r}:({adr})"
    else:
        r, adr, x = args
        return f"{r}:({adr}+{x})"

# ビットシフト  
def SL(opr):
    args = opr.split(',')
    if len(args) ==2:
        r, adr = args
        return f"{r}<-{r} << {adr}"
    else:
        r, adr, x = args
        return f"{r}<-{r} << {adr}+{x}"

def SR(opr):
    args = opr.split(',')
    if len(args) ==2:
        r, adr = args
        return f"{r}<-{r} >> {adr}"
    else:
        r, adr, x = args
        return f"{r}<-{r} >> {adr}+{x}"
    
# JUMP系
def JMI(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"SF=1 then goto {opr}"
    else:
        adr, x = args
        return f"SF=1 then goto {adr}+{x}"

def JNZ(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"ZF=0 then goto {opr}"
    else:
        adr, x = args
        return f"ZF=0 then goto {adr}+{x}"

def JZE(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"ZF=1 then goto {opr}"
    else:
        adr, x = args
        return f"ZF=1 then goto {adr}+{x}"

def JPL(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"SF=0 & ZF=0 then goto {opr}"
    else:
        adr, x = args
        return f"SF=0 & ZF=0 then goto {adr}+{x}"

def JOV(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"OF=1 then goto {opr}"
    else:
        adr, x = args
        return f"OF=1 then goto {adr}+{x}"

def JUMP(opr):
    args = opr.split(',')
    if len(args) ==1:
        return f"goto {opr}"
    else:
        adr, x = args
        return f"goto {adr}+{x}"

# stack系
def PUSH(opr):
    args = opr.split(',')
    if len(args) == 1:
        adr = args
        return f"SP<-SP-1, <SP><-{adr}"
    else:
        adr, x = args
        return f"SP<-SP-1, <SP><-{adr}+{x}"

def POP(opr):
    return f"(SP)->{opr}, <SP><-SP+1"


COMMENT_RULES = {
    "DC": DC,
    "DS": DS,
    "LD": LD,
    "LAD": LAD,
    "ST": ST,

    "ADDA": ADD,
    "ADDL": ADD,
    "SUBA": SUB,
    "SUBL": SUB,

    "CPA": CP,
    "CPL": CP,

    "SLA": SL,
    "SLL": SL,
    "SRA": SR,
    "SRL": SR,

    "JMI": JMI,
    "JNZ": JNZ,
    "JZE": JZE,
    "JPL": JPL,
    "JOV": JOV,
    "JUMP": JUMP,

    "PUSH": PUSH,
    "POP": POP,

    "CALL": JUMP
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