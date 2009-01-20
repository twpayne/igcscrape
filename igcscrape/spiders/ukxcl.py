# -*- coding: utf8 -*-
#
#   UKXCL IGC scraper
#   Copyright (C) 2009  Tom Payne
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import with_statement

from cgi import parse_qs
import os
import os.path

from scrapy.link.extractors import RegexLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class UkxclSpider(CrawlSpider):
    domain_name = 'pgcomps.org.uk'
    start_urls = ['http://www.pgcomps.org.uk/xcleague/xcl_past.htm']

    rules = (Rule(RegexLinkExtractor(
                 allow=(r'www.pgcomps.org.uk/xcleague/xc/view.php', ))),
             Rule(RegexLinkExtractor(
                 allow=(r'www.pgcomps.org.uk/xcleague/xc/viewFlight.php', ),
                 restrict_xpaths=('//a[parent::td[@class="flightIgc"]]', ))),
             Rule(RegexLinkExtractor(
                 allow=(r'www.pgcomps.org.uk/xcleague/xc/download.php',),
                 restrict_xpaths=('//a[text()="Download IGC"]',)),
                 'save_igc', follow=False))

    def save_igc(self, response):
        tracklog = parse_qs(response.url.query)['tracklog'][0]
        year, filename = tracklog.split('/')[-2:]
        path = os.path.join('ukxcl', year)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, filename), 'w') as file:
            file.write(str(response.body))


SPIDER = UkxclSpider()
