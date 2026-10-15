sherst = input("собака короткошерстной породы? ").lower()
if sherst == "да":
    rost = input("рост собаки менее 50 см? ").lower()
    if rost == "да":
        print("такса")
    else:
        print("доберман")
else:
    rost = input("Рост собаки менее 50 см? ").lower()
    if rost == "да":
        print("сенбернар")
    else:
        rost = input("У собаки рост менее 70 см? ").lower()
        if rost == "да":
            ushi = input("У собаки длинные уши? ").lower()
            if ushi == "да":
                print("бассет")
            else:
                print("колли")
        else:
            print("сенбернар")