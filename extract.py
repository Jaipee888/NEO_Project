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

import models


neo_list = list()
closeApproach_list = list()
pdes_name = dict()


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)

        if not neo_list:
            for row in reader:
                name = dict(row).get('name')

                if not name:
                    name = None

                pdes = dict(row).get('pdes')

                if not pdes:
                    pdes = "nan"

                dia = dict(row).get('diameter')
                if dia:
                    dia = float(dia)
                else:
                    dia = float("nan")

                haz = dict(row).get('pha')
                if haz == "Y":
                    haz = True
                else:
                    haz = False

                neoObjAttr = models.NearEarthObject(name=name, designation=pdes, diameter=dia, hazardous=haz)
                neo_list.append(neoObjAttr)
                pdes_name[pdes] = neoObjAttr

    file.close()
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    if len(pdes_name) == 0:
        c = load_neos(neo_csv_path)

    with open(cad_json_path) as f:
        data = json.load(f)
        if not closeApproach_list:
            for val in data['data']:
                neo_name = pdes_name[val[0]]
                closeApproach_list.append(
                    models.CloseApproach(designation=val[0], time=val[3], distance=float(val[4]),
                                         velocity=float(val[7]),
                                         neo=neo_name))

    f.close()
    return closeApproach_list
