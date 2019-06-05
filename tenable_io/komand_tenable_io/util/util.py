def folder_verify(conn, logger):
    try:
        folder = conn.folder_helper.create(name='test')
        folder.delete()
        return "Connection successful"
    except Exception as e:
        logger.error("Connection failed. Error: " + str(e))