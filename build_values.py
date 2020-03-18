
import csv, sys

def build_count_list(cin, i):
    """
    First builds a dictionary keyed by the value in position i of the .csv file,
    with value the count of the number of entries in the file with that value
    :param cin: an open csv file with the header already read
    :param i: the index of the column whose value is to be counted
    :return: A list of [value, count] sorted in descending order by count
    """
    count_d = {}
    for l in cin:
        count_d[l[i]] = count_d.setdefault(l[i], 0) + 1

    count_l = []
    for k,v in count_d.items():
        count_l.append([k,v])
    count_l.sort(key = lambda l: l[1], reverse = True)
    return count_l


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python build_values.py in.csv out.csv index')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    cin = csv.reader(fin)
    fout = open(sys.argv[2], 'w')
    cout = csv.writer(fout)
    i = int(sys.argv[3])

    h = next(cin)
    cout.writerow([h[i], 'Count'])

    count_l = build_count_list(cin, i)

    cout.writerows(count_l)

    fin.close()
    fout.close()