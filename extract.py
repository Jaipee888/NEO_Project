"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.

    neo_list = list()

    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = dict(row).get('name')
            pdes = dict(row).get('pdes')
            dia = dict(row).get('diameter')
            haz = dict(row).get('pha')
            neo_list.append({'name': name, 'pdes': pdes, 'diameter': dia, 'pha': haz})

    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    closeApproach_list = list()
    with open(cad_json_path) as f:
        data = json.load(f)
        # for val in data['data']:
        #     for element in val:
        #         print("Element is: ", element)
        #         print("Val is: ", val)
        #         closeApproach_list.append({'des': val[0], 'cd': val[3], 'dist':val[4], 'v_rel':val[7]})
        #         break

        for val in data['data']:
            closeApproach_list.append({'des': val[0], 'cd': val[3], 'dist': val[4], 'v_rel': val[7]})

    return closeApproach_list
