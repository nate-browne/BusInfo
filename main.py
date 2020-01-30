#!/usr/bin/env python3
from sys import exit

import busmonitor as bm
from custexcept import APIException, APIInitException

cmd_str = "Commands: get (a)gencies, get (r)outes for agency, get route (i)nfo\
, get arrivals for (s)top, get s(c)hedule"

if __name__ == '__main__':

    try:
        bus = bm.BusMonitor()
    except APIInitException as e:
        print(e)
        print()
        exit(1)

    print()
    print("*" * 54)
    print('            WELCOME TO THE BUS ROUTE MONITOR')
    print("*" * 54)
    print()

    muni = input('use muni (y/n)? ')
    muni = muni.upper()

    agncy = "San Francisco Muni" if muni == 'Y' else ""

    while True:

        print()
        print(cmd_str)
        try:
            cmd = input("Enter an option: ")
        except (KeyboardInterrupt, EOFError):
            print()
            break

        cmd = cmd.upper()

        try:
            if cmd == 'A':

                code, res = bus.get_agencies()
                if code == 200:
                    print()
                    for tag, title in res:
                        print(f'\t{tag} - {title}')
                else:
                    print("\t\nInvalid response received from server.")

            elif cmd == 'R':

                prmpt = "Enter an agency name (not code): "
                agency = agncy if agncy != "" else input(prmpt)
                res = bus.get_routes_for(agency)
                print()
                for ent in res:
                    print(ent)

            elif cmd == 'I':

                prmpt = "Enter an agency name (not code): "
                agency = agncy if agncy != "" else input(prmpt)
                route = input("Enter a route tag to get info for: ")
                res = bus.get_route_info_for(agency, route)
                print()
                for title, stopID in res:
                    print(f'{stopID} - {title}')

            elif cmd == 'S':
                pass
            elif cmd == 'C':
                pass
            else:
                print("\n\tInvalid command entered.")
        except APIException as e:
            print(e)
