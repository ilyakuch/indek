def slv(ränta: float, år: int):
    return (1+ränta)**år

def nuv(ränta: float, år: int):
    return 1/((1+ränta)**år)

def nus(ränta: float, år: int):
    return (1-(1+ränta)**(-år))/ränta

def ann(ränta: float, år: int):
    return ränta/(1-(1+ränta)**(-år))



def main():
    modes = {
        "slv": slv,
        "nuv": nuv,
        "nus": nus,
        "ann": ann
    }

    mode: str = input("*: ")
    ränta = int(input("*: "))
    år = int(input("*: "))

    if mode in modes:
        result = modes[mode](ränta/100, år)
        print(round(result, 3))
    else:
        ...

if __name__ == "__main__":
    while True:
        main()