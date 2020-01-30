#!/usr/bin/env python3
import pprint
import requests
from typing import List, Tuple

from custexcept import APIException, APIInitException

InfoTuple = Tuple[str, str]

_AG = "http://webservices.nextbus.com/service/publicJSONFeed?command={cmd}"

agency_tag = '&a={}'
route_tag = '&r={}'
stop_tag = '&s={}'
id_tag = '&stopId={}'


class BusMonitor(object):

    def __init__(self, debug: bool = False):
        self._agencies = dict()
        code, tmp = self.get_agencies()

        if code != 200:
            raise APIInitException("Could not get agencies.")

        for tag, title in tmp:
            self._agencies[title] = tag

        self.pp = pprint.PrettyPrinter(indent=1)
        self.debug = debug

    def get_agencies(self) -> Tuple[int, List[InfoTuple]]:
        '''
        Return all agencies that the app can use.\n
        Params: none\n
        Returns: a status code, list of tuples of codes to agencies
        '''
        agencies = requests.get(_AG.format(cmd="agencyList"))

        if agencies.status_code != requests.codes['ok']:
            return 400, []

        agencies = agencies.json()

        res = []
        for ent in agencies['agency']:
            res.append((ent['tag'], ent['title']))

        return 200, res

    def get_routes_for(self, agency: str) -> List[str]:
        '''
        Return all possible routes for a given agency.\n
        Params:
                agency - Name of the agency to use\n
        Returns:
                list of routes\n
        '''
        if agency not in self._agencies:
            raise APIException("Unknown agency provided.")

        query = _AG.format(cmd="routeList") +\
            agency_tag.format(self._agencies[agency])

        rtes = requests.get(query)

        if rtes.status_code != requests.codes['ok']:
            raise APIException("Invalid response received from server.")

        rtes = rtes.json()

        if self.debug:
            self.pp.pprint(rtes)

        rt_lst = rtes['route']

        res = []
        for ent in rt_lst:
            res.append(f'{ent["title"]}')

        if self.debug:
            self.pp.pprint(res)

        return res

    def get_route_info_for(self, agency: str, route: str) -> List[InfoTuple]:
        '''
        Get information for a particular agency's route.\n
        Params:
                agency - which transit agency to use.\n
                route - which route to use.\n
        Return:
                The route information
        '''
        if agency not in self._agencies:
            raise APIException('Unknown agency provided.')

        query = _AG.format(cmd="routeConfig") +\
            agency_tag.format(self._agencies[agency]) + route_tag.format(route)

        rtes = requests.get(query)

        if rtes.status_code != requests.codes['ok']:
            raise APIException('Invalid response received from server.')

        rtes = rtes.json()

        ret = []
        for obj in rtes['route']['stop']:
            ret.append((obj['title'], obj['stopId']))

        if self.debug:
            self.pp.pprint(ret)

        return ret

    def get_arrivals_for(self, agency: str, stop: str) -> List[str]:
        '''
        Gets all arrivals for a particular stop, regardless of the route.\n
        Params:
                agency - which transit agency to use.\n
                stop - which stop to use.\n
        Return:
                A list of stops
        '''
        if agency not in self._agencies:
            raise APIException('Unknown agency provided.')

        query = _AG.format(cmd="predictions") +\
            agency_tag.format(self._agencies[agency]) + id_tag.format(stop)

        rtes = requests.get(query)

        if rtes.status_code != requests.codes['ok']:
            raise APIException('Invalid response received from server.')

        rtes = rtes.json()

        return None

    def get_schedule_for(self, agency: str, route: str) -> List[str]:
        '''
        Get schedule for a particular route.\n
        Params:
                agency - which transit agency to use.\n
                route - which route to use.\n
        Return:
                A list consisting of a schedule.
        '''
        if agency not in self._agencies:
            raise APIException('Unknown agency provided.')

        query = _AG.format(cmd="schedule") +\
            agency_tag.format(self._agencies[agency]) + route_tag.format(route)

        rtes = requests.get(query)

        if rtes.status_code != requests.codes['ok']:
            raise APIException('Invalid response received from server.')

        rtes = rtes.json()

        return None
