import operator

import filters as ft


class NEODatabase:
    """
    A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """

        # # # TODO: What additional auxiliary data structures will be useful?
        # # # TODO: Link together the NEOs and their close approaches.

        self.listneo = neos
        self.listapproach = approaches

        for values in self.listapproach:
            values.neo.approaches.append(values)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """

        for desig in self.listneo:
            if desig.designation == designation:
                return desig

        return

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.

        for val in self.listneo:
            if val.name == name:
                return val

        return

    def query(self, filtDict=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """

        # TODO: Generate `CloseApproach` objects that match all of the filters.
        simple_date = filtDict["date"]
        start_date = filtDict['start_date']
        end_date = filtDict['end_date']
        max_distance = filtDict['distance_max']
        min_distance = filtDict['distance_min']
        max_velocity = filtDict['velocity_max']
        min_velocity = filtDict['velocity_min']
        max_diameter = filtDict['diameter_max']
        min_diameter = filtDict['diameter_min']
        haz = filtDict['hazardous']

        # Logic for counter values.
        arg_counter = 0
        for v in filtDict.values():
            if v:
                arg_counter = arg_counter + 1

        # print("The value of arg counter is: ", arg_counter)

        for approach in self.listapproach:

            final_counter = 0

            if simple_date:
                dt = ft.DateFilter(operator.eq, simple_date)

                if dt(approach):
                    final_counter += 1
                else:
                    continue

            if start_date:
                dt_start = ft.DateFilter(operator.ge, start_date)
                if dt_start(approach):
                    final_counter += 1
                else:
                    continue

            if end_date:
                dt_end = ft.DateFilter(operator.le, end_date)
                if dt_end(approach):
                    final_counter += 1
                else:
                    continue

            if max_distance:
                dt_distance = ft.DistanceFilter(operator.le, max_distance)
                if dt_distance(approach):
                    final_counter += 1
                else:
                    continue

            if min_distance:
                dt_distance = ft.DistanceFilter(operator.ge, min_distance)
                if dt_distance(approach):
                    final_counter += 1
                else:
                    continue

            if min_velocity:
                dt_velocity = ft.VelocityFilter(operator.ge, min_velocity)
                if dt_velocity(approach):
                    final_counter += 1
                else:
                    continue

            if max_velocity:
                dt_velocity = ft.VelocityFilter(operator.le, max_velocity)
                if dt_velocity(approach):
                    final_counter += 1
                else:
                    continue

            if min_diameter:
                dt_diameter = ft.DiameterFilter(operator.ge, min_diameter)
                if dt_diameter(approach):
                    final_counter += 1
                else:
                    continue

            if max_diameter:
                dt_diameter = ft.DiameterFilter(operator.le, max_diameter)
                if dt_diameter(approach):
                    final_counter += 1
                else:
                    continue

            if haz:
                dt_haz = ft.HazardFilter(operator.eq, haz)
                if dt_haz(approach):
                    final_counter += 1
                else:
                    continue

            if final_counter == arg_counter:
                yield approach
            else:
                continue

        return

