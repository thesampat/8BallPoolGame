# training data
training_data = [['brown', 10, 'Kivi'],
                 ['orange', 9, 'Orange'],
                 ['brown', 10, 'Kivi'],
                 ['red', 10, 'Apple'],
                 ['brown', 4, 'Kivi'],
                 ['yellow', 8, 'Mango']]


def unique(dataset, col):
    U_values = set([row[col] for row in dataset])
    return U_values


def get_counts(dataset):
    counts = {}
    for row in dataset:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def partation(question, col, dataset):
    true_rows = []
    false_rows = []
    for row in dataset:
        if row[col] is question:
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def gini(rows):
    counts = get_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity


def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


def best_split(dataset):
    n_col = len(dataset[0]) - 1
    best_question = ''
    best_gain = 0
    selected_col = 0
    current_impurity = gini(dataset)
    for col in range(n_col):
        # print(col, 'colums_numbers')
        values = (unique(dataset, col))
        for question in values:
            true_rows, false_rows = partation(question, col, dataset)
            gain = info_gain(true_rows, false_rows, current_impurity)
            if gain > best_gain:
                print(col, 'lastcol')
                best_gain, best_question, selected_col = gain, question, col
    return best_gain, best_question, selected_col


def build_tree(dataset, count):
    # Return if leaf node
    if len(dataset) is 0 or gini(dataset) == 0.5:
        print(gini(dataset))
        return

    best_gain, best_question, col = best_split(dataset)

    true_branch, false_branch = partation(best_question, col, dataset)
    print(best_question, '---Question--')
    print(true_branch, count, '-----true-----', end='\n')
    print(false_branch, count, '___false___')
    # print(gini(true_branch), 'true', count)
    # print(gini(false_branch), 'false', count)

    if gini(true_branch) > 0.0:
        count += 1
        build_tree(true_branch, count)

    if gini(false_branch) > 0.0:
        count += 1
        build_tree(false_branch, count)
    # print('take')
    return



training_data2 = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
    ['Yellow', 1, 'Apple']
]
# print(len(training_data[0]))
build_tree(training_data, 1)
