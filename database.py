"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""

import models


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

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
        self.neos = neos
        self.approaches = approaches
        # TODO: What additional auxiliary data structures will be useful?

        # TODO: Link together the NEOs and their close approaches.
        self.nearEarthObject = models.NearEarthObject()
        self.closeApproachObject = models.CloseApproach()


    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.
        for values in range(0, len(self.neos)):
            if self.neos[values].get('pdes') == designation:
                self.closeApproachObject.neo = self.neos[values]
                self.nearEarthObject.name = self.neos[values].get('name')
                self.nearEarthObject.designation = self.neos[values].get('pdes')
                self.nearEarthObject.diameter = self.neos[values].get('diameter')
                self.nearEarthObject.hazardous = self.neos[values].get('pha')
                break
            else:
                continue

        if self.nearEarthObject.designation == None:
            return

        for cValues in range(0, len(self.approaches)):
            if self.approaches[cValues].get('des') == designation:
                self.nearEarthObject.approaches.append(self.approaches[cValues])

        return self.nearEarthObject

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

        for nameVal in range(0, len(self.neos)):
            if self.neos[nameVal].get('name') == name:
                self.closeApproachObject.neo = self.neos[nameVal]
                self.nearEarthObject.name = self.neos[nameVal].get('name')
                self.nearEarthObject.designation = self.neos[nameVal].get('pdes')
                self.nearEarthObject.diameter = self.neos[nameVal].get('diameter')
                self.nearEarthObject.hazardous = self.neos[nameVal].get('pha')
                break
            else:
                continue

        if self.nearEarthObject.name == None:
            return

        for appr in range(0, len(self.approaches)):
            if self.approaches[appr].get('des') == self.nearEarthObject.designation:
                self.nearEarthObject.approaches.append(self.approaches[appr])
        return self.nearEarthObject

    def query(self, filters=()):
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
        for approach in self._approaches:
            yield approach
