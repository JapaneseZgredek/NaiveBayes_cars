from Specifications import Specifications


def read_from_file() -> list:
    data = []
    with open("car_evaluation.data", "r") as file:
        for line in file:
            line = line.split(',')
            data.append(Specifications(line[:6], line[len(line) - 1].removesuffix('\n')))
    return data


def main():
    data = read_from_file()
    for element in data:
        element.to_string()



if __name__ == '__main__':
    main()
