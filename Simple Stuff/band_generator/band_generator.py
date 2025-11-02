def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet name?\n")
    band_name = city_name + " " + pet_name
    band_name_join = " ".join([city_name, pet_name])
    print(f"Your band name could be {city_name} {pet_name}")
    print(f"Your band name could be {band_name}")
    print(f"Your band name could be {band_name_join}")



def main():
    band_name_generator()

if __name__ == "__main__":
    main()