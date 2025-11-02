import random

def banker_roulette_loop():
    names = []
    print("Provide every name")
    while True:
        name = input().strip()
        if name == "":
            break
        names.append(name)
    if not names:
        return
    chosen_name = random.randint(0, len(names)-1)
    print(f"Person paying is {names[chosen_name]}")

def banker_roulette():
    names_string = input("Provide every name seperated by a comma ")
    names_list = names_string.split(",")
    chosen_name = random.randint(0, len(names_list) -1)
    print(f"Person paying is {names_list[chosen_name]}")

def main():
    banker_roulette_loop()

if __name__ == "__main__":
    main()