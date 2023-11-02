from Specifications import Specifications

size_vgood = 0
size_acc = 0
size_good = 0
size_unacc = 0
vgood_correct = 0
vgood_total = 0
acc_total = 0
acc_correct = 0
good_total = 0
good_correct = 0
unacc_correct = 0
unacc_total = 0


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
    return testing_data, training_data


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


def calculate_possibility(dictionaries_of_opinion: list, specification: Specifications, size_of_data: int, size_of_specific_verdict: int, data_dictionaries: list) -> float:
    possibility = size_of_specific_verdict / size_of_data
    for i in range(len(specification.attributes)):
        if specification.attributes[i] in dictionaries_of_opinion[i]:
            possibility *= (dictionaries_of_opinion[i][specification.attributes[i]] / size_of_specific_verdict)
        else:
            possibility *= (1/(size_of_specific_verdict+len(data_dictionaries[i])))
    return possibility


def calculate_correctness_of_algorithm(list_of_dictionaries: list, list_of_lists_seperated_by_specification_attributes: list):
    global vgood_correct
    global vgood_total
    global acc_correct
    global acc_total
    global good_correct
    global good_total
    global unacc_correct
    global unacc_total
    correct_guesses = 0
    for specification in list_of_lists_seperated_by_specification_attributes[4]:
        possibilities = [calculate_possibility(dictionaries_of_opinion=list_of_dictionaries[0], specification=specification, size_of_data=len(list_of_lists_seperated_by_specification_attributes[3]), size_of_specific_verdict=len(list_of_lists_seperated_by_specification_attributes[0]), data_dictionaries=list_of_dictionaries[3]),
                         calculate_possibility(dictionaries_of_opinion=list_of_dictionaries[1], specification=specification, size_of_data=len(list_of_lists_seperated_by_specification_attributes[3]), size_of_specific_verdict=len(list_of_lists_seperated_by_specification_attributes[1]), data_dictionaries=list_of_dictionaries[3]),
                         calculate_possibility(dictionaries_of_opinion=list_of_dictionaries[2], specification=specification, size_of_data=len(list_of_lists_seperated_by_specification_attributes[3]), size_of_specific_verdict=len(list_of_lists_seperated_by_specification_attributes[2]), data_dictionaries=list_of_dictionaries[3]),
                         calculate_possibility(dictionaries_of_opinion=list_of_dictionaries[3], specification=specification, size_of_data=len(list_of_lists_seperated_by_specification_attributes[3]), size_of_specific_verdict=len(list_of_lists_seperated_by_specification_attributes[3]), data_dictionaries=list_of_dictionaries[3])]

        what_opinion = 'vgood' if possibilities.index(max(possibilities)) == 0 else \
                           'acc' if possibilities.index(max(possibilities)) == 1 else \
                           'good' if possibilities.index(max(possibilities)) == 2 else \
                           'unacc' if possibilities.index(max(possibilities)) == 3 else 'This should not happen'

        if what_opinion == specification.opinion:
            if what_opinion == 'vgood':
                vgood_correct += 1
                vgood_total += 1
            elif what_opinion == 'acc':
                acc_correct += 1
                acc_total += 1
            elif what_opinion == 'good':
                good_correct += 1
                good_total += 1
            elif what_opinion == 'unacc':
                unacc_correct += 1
                unacc_total += 1
            correct_guesses += 1
        else:
            if specification.opinion == 'vgood':
                vgood_total += 1
            elif specification.opinion == 'acc':
                acc_total += 1
            elif specification.opinion == 'good':
                good_total += 1
            elif specification.opinion == 'unacc':
                unacc_total += 1

    return correct_guesses


def main():
    training_data, testing_data = read_from_file()
    vgood, acc, good, unacc = cut_data_into_lists(training_data)
    data_dictionary = create_dictionaries_for_specific_opinion(training_data)

    vgood_dict = create_dictionaries_for_specific_opinion(vgood)
    acc_dict = create_dictionaries_for_specific_opinion(acc)
    good_dict = create_dictionaries_for_specific_opinion(good)
    unacc_dict = create_dictionaries_for_specific_opinion(unacc)

    correct_guesses = calculate_correctness_of_algorithm(
        [vgood_dict, acc_dict, good_dict, unacc_dict, data_dictionary],
        [vgood, acc, good, unacc, testing_data])

    print(f'Correctness {correct_guesses/len(testing_data)}%     ---     {correct_guesses}/{len(testing_data)}')
    print(f'Vgood: {vgood_correct}/{vgood_total}')
    print(f'Acc: {acc_correct}/{acc_total}')
    print(f'Good:  {good_correct}/{good_total}')
    print(f'Unacc: {unacc_correct}/{unacc_total}')


if __name__ == '__main__':
    main()
