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


def cut_data_into_lists(data: list):
    vgood, acc, good, unacc = [], [], [], []
    for specification in data:
        if specification.opinion == 'vgood':
            vgood.append(specification)
        elif specification.opinion == 'acc':
            acc.append(specification)
        elif specification.opinion == 'good':
            good.append(specification)
        else:
            unacc.append(specification)

    return vgood, acc, good, unacc


def create_dictionaries_for_specific_opinion(opinion_list: list) -> list:
    dictionaries_list = [{}, {}, {}, {}, {},{}]
    for specification in opinion_list:
        for i in range(len(specification.attributes)):
            if specification.attributes[i] in dictionaries_list[i]:
                dictionaries_list[i][specification.attributes[i]] += 1
            else:
                dictionaries_list[i][specification.attributes[i]] = 1

    return dictionaries_list


def main():
    training_data, testing_data = read_from_file()
    vgood, acc, good, unacc = cut_data_into_lists(training_data)
    data_dictionary = create_dictionaries_for_specific_opinion(training_data)
    print(data_dictionary)


if __name__ == '__main__':
    main()
