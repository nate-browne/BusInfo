# Nate's Bus Info Tool
### Introduction
This is a useless little python script that can be used to
pull information about transit systems.

It's powered by the [NextBus API](https://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)
(more documentation [here](https://gist.github.com/grantland/7cf4097dd9cdf0dfed14)), which is a
free way to pull information about select rotes. Fair warning, the returned XML/JSON is
somewhat hard to parse so if you wanna add functionality feel free but it'll be annoying.

### How to Use
Currently, there are only three pieces of functionality present. The first is that you are
able to see the list of agencies supported. The second is that you can see the routes for
a particular agency. The last is that you can see information about a particular route
from a particular agency.

*Other pieces of functionality may be added later if I feel like it.*

### Contributing
I'm not taking PRs but feel free to fork your own version and do
whatever you want.
