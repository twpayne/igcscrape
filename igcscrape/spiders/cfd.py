# -*- coding: utf8 -*-
#
#   CFD IGC scraper
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

from scrapy.link.extractors import RegexLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class CfdSpider(CrawlSpider):
    domain_name = 'ffvl.fr'
    start_urls = ['http://parapente.ffvl.fr/cfd']

    rules = (Rule(RegexLinkExtractor(
                 allow=(r'parapente.ffvl.fr/node/894/\d+$',))),
             Rule(RegexLinkExtractor(
                 allow=(r'parapente.ffvl.fr/cfd/liste/\d+(\?page=\d+)?$',))),
             Rule(RegexLinkExtractor(
                 allow=(r'parapente.ffvl.fr/cfd/liste/\d+/vol/\d+$',),
                 restrict_xpaths=('//a[text()="gps"]',))),
             Rule(RegexLinkExtractor(
                 allow=(r'cfd.ffvl.fr/cfd/getIgcFile.php', ),
                 restrict_xpaths=('//a[text()="IGC"]',)),
                 'save_igc', follow=False))

    def save_igc(self, response):
        pairs = response.url.query.split('&')
        filename = dict(pair.split('=', 2) for pair in pairs)['pIgcFile']
        with open(filename, 'w') as file:
            file.write(str(response.body))


SPIDER = CfdSpider()
