import komand
import time
from .schema import MonitorInput, MonitorOutput
# Custom imports below
import ftputil
import stat
from array import array
import base64
import hashlib
import os


class Monitor(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='monitor',
            description='Poll for files or directory changes',
            input=MonitorInput(),
            output=MonitorOutput())

    def run(self, params={}):
        """Run the trigger"""
        # send a test event
        # Stored data for file
        stored_file_attribs = array('I')
        # Stored data for directory
        stored_dir_attribs = {}
        # Disable caching so we can see changes
        self.connection.ftp_host.stat_cache.disable()

        while True:
            # Get parameters
            path = params.get('path')
            monitor_time = params.get('monitor_time', False)
            monitor_size = params.get('monitor_size', True)
            monitor_mode = params.get('monitor_mode', False)
            interval = params.get('interval', 300)
            dir_test = None
            # Get information on path passed in
            try:
                dir_test = ftputil.FTPHost.lstat(self.connection.ftp_host, path)
            except ftputil.error.FTPError as e:
                raise e
            modedir = dir_test.st_mode
            # See if path passed in is a directory
            is_dir = stat.S_ISDIR(modedir)
            # Has directory changed?  Initially no.
            has_changed = False
            # If it's a directory
            if is_dir:
                dir_attribs = {}
                names = self.connection.ftp_host.listdir(path)
                for name in names:
                    lstatval = ftputil.FTPHost.lstat(self.connection.ftp_host, name)
                    # Populate tmp_array with values to be tracked
                    tmp_array = array('I')
                    if monitor_size:
                        tmp_array.append(lstatval.st_size)
                        self.logger.info(path + "/" + name + " size is " + str(lstatval.st_size))
                    if monitor_time:
                        tmp_array.append(int(lstatval.st_mtime))
                        self.logger.info(path + "/" + name + " time is " + time.ctime(int(lstatval.st_mtime)))
                    if monitor_mode:
                        tmp_array.append(lstatval.st_mode)
                        self.logger.info(path + "/" + name + " mode is " + str(lstatval.st_mode))
                    # Populate dictionary with current values
                    dir_attribs[name] = tmp_array

                if dir_attribs != stored_dir_attribs:
                    # If we're not just starting out
                    if len(stored_dir_attribs.keys()) > 0:
                        has_changed = True
                    # Store information about directory
                    stored_dir_attribs = dir_attribs
                    names2 = '\n'.join(self.connection.ftp_host._dir(path))
                    if has_changed:
                        self.send({'changed': names2})
            # If it's just a file
            else:
                # Populate file_attribs with values to be tracked
                file_attribs = array('I')
                if monitor_size:
                    file_attribs.append(dir_test.st_size)
                    self.logger.info(path + " size is " + str(dir_test.st_size))
                if monitor_time:
                    file_attribs.append(int(dir_test.st_mtime))
                    self.logger.info(path + " time is " + time.ctime(int(dir_test.st_mtime)))
                if monitor_mode:
                    file_attribs.append(dir_test.st_mode)
                    self.logger.info(path + " mode is " + str(dir_test.st_mode))
                if file_attribs != stored_file_attribs:
                    if len(stored_file_attribs) > 0:
                        has_changed = True
                    # Store file information
                    stored_file_attribs = file_attribs
                    # If it's changed
                    if has_changed:
                        # Get tmp local file name based on MD5 hash of path + time
                        millis = int(round(time.time() * 1000))
                        tmp_str = path + str(millis)
                        tmp_filename = hashlib.md5(tmp_str.encode('utf-8')).hexdigest()
                        # Actually download file
                        try:
                            self.connection.ftp_host.download(path, tmp_filename)
                        except ftputil.error.FTPError as e:
                            raise e
                        # Encode file as base64
                        with open(tmp_filename, 'rb') as f:
                            encoded = base64.b64encode(f.read()).decode('utf-8')
                            #Clean up temporary file
                            os.remove(tmp_filename)
                            change_dict = {'changed': encoded}
                            if monitor_size:
                                change_dict['size'] = file_attribs[0]
                            if monitor_time:
                                if monitor_size:
                                    change_dict['time'] = time.ctime(file_attribs[1])
                                else:
                                    change_dict['time'] = time.ctime(file_attribs[0])
                            if monitor_mode:
                                mode_index = len(file_attribs) - 1
                                change_dict['mode'] = file_attribs[mode_index]
                            self.send(change_dict)

            time.sleep(interval)

    def test(self):
        """TODO: Test the trigger"""
        return {}

