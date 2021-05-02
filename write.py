"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""

import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name',
                  'diameter_km', 'potentially_hazardous')

    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for tmp_dict in results:
            ans_dict = next(tmp_dict)
            writer.writerow({'datetime_utc': ans_dict.time, 'distance_au': ans_dict.distance,
                             'velocity_km_s': ans_dict.velocity, 'designation': ans_dict.designation,
                             'name': ans_dict.neo.name,
                             'diameter_km': ans_dict.neo.diameter, 'potentially_hazardous': ans_dict.neo.hazardous})

        # for tmp_dict in results:
        #     ans_dict = next(tmp_dict)
        #     ans_dict = {k: "NaN" if not v else v for k, v in ans_dict.items()}
        #     writer.writerow(
        #         {'datetime_utc': ans_dict['cd'], 'distance_au': ans_dict['dist'], 'velocity_km_s': ans_dict['v_rel'],
        #          'designation': ans_dict['des'], 'name': ans_dict['name'], 'diameter_km': ans_dict['diameter'],
        #          'potentially_hazardous': ans_dict['pha']})


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    final_json = list()
    with open(filename, "w") as write_file:
        for itemp in results:
            json_dict = next(itemp)

            final_dict = {'datetime_utc': json_dict.time_str, 'distance_au': json_dict.distance,
                          'velocity_km_s': json_dict.velocity,
                          'designation': json_dict.designation,
                          "neo": {
                              'name': json_dict.neo.name, 'diameter_km': json_dict.neo.diameter,
                              'potentially_hazardous': json_dict.neo.hazardous
                          }
                          }
            final_json.append(final_dict)
            print(final_json)

        json.dump(final_json, write_file, indent=5)
