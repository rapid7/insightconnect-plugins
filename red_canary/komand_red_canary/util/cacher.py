import komand
import maya


def load_cache(file_name: str, suffix: str, logger, force_offset, date_offset=None):
    cache_file_name = file_name + suffix
    cached_date = None

    # Create, or load data from cache
    with komand.helper.open_cachefile(cache_file_name) as cache_file:
        logger.info("[*] Found or created cache file: {}".format(cache_file_name))
        # set date to what was cached. Using maya to parse string
        # logger.info(cache_file.readlines())

        date_from_file = cache_file.readline()

        # Set from cache if cache exists and not forces to use offset
        if date_from_file and force_offset is False:
            cached_date = maya.parse(date_from_file).datetime()
            logger.info("[*] Setting date from cache!")
            logger.info("[*] Writing updated time to cache")
            cache_file.write(str(cached_date))
            return cache_file_name, cached_date

        # Set from offset and force set from offset
        if date_offset and force_offset is True:
            cached_date = maya.MayaDT.from_rfc3339(date_offset).datetime()
            logger.info("[*] Setting date from forced offset")
            logger.info("[*] Writing updated time to cache")
            cache_file.write(str(cached_date))
            return cache_file_name, cached_date

        if not cached_date:
            # Set from offset if not forced and no cached date exists
            if date_offset and force_offset is False:
                cached_date = maya.MayaDT.from_rfc3339(date_offset).datetime()
                logger.info("[*] Setting date from offset and not forced")
                logger.info("[*] Writing updated time to cache")
                cache_file.write(str(cached_date))
                return cache_file_name, cached_date
            # Set if no offset, force offset or cached date exists
            if not cached_date and not date_offset:
                cached_date = maya.now().datetime()
                logger.info("[*] No date from cache or offset, setting time from now")
                logger.info("[*] Writing updated time to cache")
                cache_file.write(str(cached_date))
                return cache_file_name, cached_date


def cache(cache_file_name: str, event_date: str, logger):
    # Set file name

    # Create, or load data from cache
    with komand.helper.open_cachefile(cache_file_name) as cache_file:
        logger.info(
            "[*] Updating cache: {} to event date: {}".format(
                cache_file_name, event_date
            )
        )
        cache_file.write(str(event_date))
        cache_file.truncate()
