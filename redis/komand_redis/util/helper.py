from komand.exceptions import PluginException


class Helper:
    @staticmethod
    def set_expire(logger, connection, key, expire):
        expire = Helper.clear_expire(expire)

        if expire:
            logger.info(f"Setting expiration: {key}")
            connection.redis.expire(key, expire)

    @staticmethod
    def clear_expire(expire):
        if expire and int(expire) < 0:
            raise PluginException(cause='Input error',
                                  assistance='Expire should be greater than or equal 0')

        return expire
