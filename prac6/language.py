from programming_language import ProgrammingLanguage


def main():
    """ProgrammingLanguage demo"""

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python.__str__())

    dynamic_lists = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for dynamic in dynamic_lists:
        if dynamic.is_dynamic():
            print("{}".format(dynamic.filed))


if __name__ == '__main__':
    main()
