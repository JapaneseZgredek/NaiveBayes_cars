from Specifications import Specifications


def read_from_file():
    training_data = []
    testing_data = []
    with open("car_evaluation.data", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.split(',')
            if i < len(lines)*0.7:
                testing_data.append(Specifications(line[:6], line[len(line) - 1].removesuffix('\n')))
            else:
                training_data.append(Specifications(line[:6], line[len(line) - 1].removesuffix('\n')))
    return training_data, testing_data


def main():
    training_data, testing_data = read_from_file()
    for element in training_data:
        element.to_string()
    for element in testing_data:
        element.to_string()
    print(len(testing_data))
    print(len(training_data))


if __name__ == '__main__':
    main()
