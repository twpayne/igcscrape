import igcscrape

# ---------------------------------------------------------------------------
# - Scrapy settings for igcscrape                                    -
# ---------------------------------------------------------------------------

BOT_NAME = 'scrapybot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['igcscrape.spiders']
NEWSPIDER_MODULE = 'igcscrape.spiders'
TEMPLATES_DIR = '%s/templates' % igcscrape.__path__[0]
ENABLED_SPIDERS_FILE = '%s/conf/enabled_spiders.list' % igcscrape.__path__[0]
DEFAULT_ITEM_CLASS = 'scrapy.item.ScrapedItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
DOWNLOAD_TIMEOUT = 600

# use this spider class as default when no spider was found for a given url
#DEFAULT_SPIDER = 'scrapy.contrib.spiders.generic.GenericSpider'

# uncomment if you want to add your own custom scrapy commands
#COMMANDS_MODULE = 'igcscrape.commands'
#COMMANDS_SETTINGS_MODULE = 'igcscrape.conf.commands'

#Global timeout between sucessive downloads (can be overrided by spider
#attribute download_timeout
#DOWNLOAD_TIMEOUT = 0

MYSQL_CONNECTION_SETTINGS = {"charset": "utf8" }
MYSQL_CONNECTION_PING_PERIOD = 600

SCHEDULER = 'scrapy.core.scheduler.Scheduler'
SCHEDULER_ORDER = 'BFO'   # available orders: BFO (default), DFO

#CACHE2_DIR = '/tmp/cache2'  # if set, enables HTTP cache
#CACHE2_IGNORE_MISSING = 0   # ignore requests not in cache
#CACHE2_SECTORIZE = 1         # sectorize domains to distribute storage among servers

#STATS_ENABLED = 1   # enable stats
#STATS_CLEANUP = 0   # cleanup domain stats when a domain is closed (saves memory)
#STATS_DEBUG = 0     # log stats on domain closed

EXTENSIONS = (
    'scrapy.management.web.WebConsole',
    'scrapy.management.telnet.TelnetConsole',
)

DOWNLOADER_MIDDLEWARES = (
    # Engine side
    'scrapy.contrib.downloadermiddleware.errorpages.ErrorPagesMiddleware',
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware',
    'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware',
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware',
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware',
    'scrapy.contrib.downloadermiddleware.common.CommonMiddleware',
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware',
    'scrapy.contrib.downloadermiddleware.compression.CompressionMiddleware',
    'scrapy.contrib.downloadermiddleware.debug.CrawlDebug',
    'scrapy.contrib.downloadermiddleware.cache.CacheMiddleware',
    # Downloader side
)

SPIDER_MIDDLEWARES = (
    # Engine side
    'scrapy.contrib.spidermiddleware.limit.RequestLimitMiddleware',
    'scrapy.contrib.spidermiddleware.restrict.RestrictMiddleware',
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware',
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware',
    'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware',
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware',
    'scrapy.contrib.spidermiddleware.urlfilter.UrlFilterMiddleware',
    # Spider side
)

# Item pipelines are usually configured by commands (see conf/commands)
#ITEM_PIPELINES = (
#)

#DEPTH_LIMIT = 10  # limit the maximum link depth to follow
#DEPTH_STATS = 1    # enable depth stats

# Limit URL length. See: http://www.boutell.com/newfaq/misc/urllength.html
URLLENGTH_LIMIT = 2083

#WEBCONSOLE_ENABLED = 1
#WEBCONSOLE_PORT = 8060  # if not set uses a dynamic port

#TELNETCONSOLE_ENABLED = 1
#TELNETCONSOLE_PORT = 2020  # if not set uses a dynamic port

# global mail sending settings
#MAIL_HOST = 'localhost'
#MAIL_FROM = 'scrapybot@localhost'

# scrapy webservice
WS_ENABLED = 0

SPIDERPROFILER_ENABLED = 0
