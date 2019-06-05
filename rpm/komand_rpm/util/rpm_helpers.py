import komand
import json
import random
import os
import re

cache_dir = '/var/cache/rpm_plugin/'
temp_dir = '/tmp/'
yum_dir = '/etc/yum.repos.d/'

centos6_repos = []
repos = {
    'CentOS 6': ['base6', 'epel6', 'extras6', 'updates6', 'centosplus6'],
    'CentOS 7': ['base7', 'epel7', 'extras7', 'updates7', 'centosplus7'],
    'Fedora 24': ['fedora24'],
    'Fedora 25': ['fedora25'],
    'Fedora 26': ['fedora26']
}


class RPMHelper(object):
    def __init__(self, logger):
        self.logger = logger

    def update_cache(self, dic, label):
        '''updates the cache when given an info dic and a label to name it'''
        #lock_cache(package.name)
        self.logger.info("UpdateCache: Updating cache for %s" % label)
        cachefile_path = cache_dir + self._trim_epoch(label)
        os.makedirs(cache_dir, exist_ok=True)
        with open(cachefile_path, 'w+', encoding='utf-8') as f:
            json.dump(dic, f)
        self.logger.info("UpdateCache: Done updating cache for %s" % label)
        #unlock_cache(package.name)

    def check_rpm_cache(self, package_list):
        '''checks cache against package list and returns a dic'''
        for p in package_list:
            cachefile_path = cache_dir + p
            if komand.helper.check_cachefile(cachefile_path):
                self.logger.info('CheckRpmCache: Cachefile match for %s' % cachefile_path)
                with open(cachefile_path, 'r', encoding='utf-8') as f:
                    return json.loads(f.read())
            else:
                return None

    def add_repo(self, url):
        '''adds a custom repo file returns a list of added repo ids and abs file path.'''
        self.logger.info('AddRepo: Adding new repo at url %s' % url)
        #cmd = 'yum-config-manager --add-repo %s' % url
        path = '%scustom-%s.repo' % (yum_dir, int(random.random() * 1000))
        cmd = 'wget -O %s %s' % (path, url)
        proc = komand.helper.exec_command(cmd)
        if proc['rcode'] == 0:
            #output = proc['stdout'].decode('utf-8').splitlines()
            #if 'repo saved to' not in output[-1]:
                #repofile_path = '/etc/yum.repos.d/%s' % format_repofile(url)
                #try: os.remove(repofile_path)
                #except: FileNotFoundError: logging.error('File could not be found at %s' % repofile_path)
                #raise Exception(proc['stdout'] + proc['stderr'])
            #else:
                #path = output[-1].split(' ')[3].strip()
            repo_ids = self._modify_repofile(path)
            return {'path': path, 'ids': repo_ids}
        else: raise Exception('AddRepo: Repofile was not downloaded from %s' % url)

    def add_key(self, url):
        '''add key into the gpg keychain'''
        proc = komand.helper.exec_command('wget -O %stemp-gpg-key %s' % (temp_dir, url))
        if proc['rcode'] == 0:
            proc2 = komand.helper.exec_command('rpm --import %stemp-gpg-key' % temp_dir)
            if proc['rcode'] != 0: raise Exception('AddKey: Key was not imported: %s' % proc['stderr'].decode('utf-8'))
            else: self.logger.info('AddKey: Key successfully added from %s' % url)
        else: raise Exception('AddKey: Key could not be downloaded: %s' % proc['stderr'].decode('utf-8'))

    def _modify_repofile(self, path):
        '''prepares the repofile by subbing in variables and returning a list of repo ids'''
        lines = []
        repo_ids = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                m = re.match(r'\[(.*?)\]', line)

                if m:
                    custom_repo = m.group(1) + '-' + str(int(random.random() * 1000))
                    line = re.sub(m.group(1), custom_repo, line)
                    repo_ids.append(custom_repo)

                line = re.sub(r'enabled=1', r'0', line)
                line = re.sub(r'\$basearch', r'$arch', line)
                line = re.sub(r'gpgcheck=1', r'gpgcheck=0', line)
                lines.append(line)

        if not repo_ids: raise Exception('ModifyRepofile: No repo IDs in repofile')
        if not lines: raise Exception('ModifyRepofile: Writing empty repo file at %s' % path)
        with open(path, 'w+', encoding='utf-8') as f:
            f.write("".join(lines))
            self.logger.info('ModifyRepofile: Repofile modified at %s ' % path)
        return repo_ids

    def checksig(self, path):
        '''rpm -K'''
        proc = komand.helper.exec_command('rpm --checksig %s' % path)
        if proc['rcode'] != 0: raise Exception('CheckSig: ' + (proc['stdout'] + proc['stderr']).decode('utf-8'))
        self.logger.info('CheckSig: RPM package verified at %s' % path)

    def package_info(self, path):
        '''returns a dic with two strings with the package info given by an rpm query or None'''
        self.logger.info('PackageInfo: Querying package info at %s' % path)
        proc = komand.helper.exec_command('rpm -qip %s' % path)
        proc2 = komand.helper.exec_command('rpm -qp --dump %s' % path)
        if proc['rcode'] == 0 and proc2['rcode'] == 0:
            return {'package': proc['stdout'].decode('utf-8'), 'files': proc2['stdout'].decode('utf-8')}
        else:
            raise Exception('CheckSig: Package at path %s could not be queried by rpm' % path)

    def info2dic(self, info):
        '''converts a dic of strings from rpm info to a custom dictionary'''
        pi = {'found': True}
        package_lines = info['package'].splitlines()[:17]
        package_desc = info['package'].splitlines()[18]
        file_strs = info['files'].splitlines()

        files = []
        for file_str in file_strs:
            file_info = file_str.split()
            f = {}
            f['path'] = file_info[0]
            f['size'] = int(file_info[1])
            f['mtime'] = file_info[2]
            f['hash'] = file_info[3]
            f['mode'] = file_info[4]
            f['owner'] = file_info[5]
            f['group'] = file_info[6]
            f['isconfig'] = int(file_info[7])
            f['isdoc'] = int(file_info[8])
            f['rdev'] = int(file_info[9])
            f['symlink'] = file_info[10]
            files.append(f)

        for line in package_lines:
            ls = line.split(':', 1)
            title = ls[0].strip()
            content = ls[1].strip()
            if title == 'Name':
                pi['name'] = content
            elif title == 'Version':
                pi['version'] = content
            elif title == 'Release':
                pi['release'] = content
            elif title == 'Architecture':
                pi['architecture'] = content
            elif title == 'License':
                pi['license'] = content
            elif title == 'Signature':
                sig_split = content.split(',')
                sig = {}
                sig['scheme'] = sig_split[0].strip()
                sig['time'] = sig_split[1].strip()
                sig['key'] = sig_split[2].strip()
                pi['signature'] = sig
            elif title == 'Source RPM':
                pi['source'] = content
            elif title == 'Build Date':
                pi['build_date'] = content
            elif title == 'Build Host':
                pi['build_host'] = content
            elif title == 'Relocations':
                pi['relocations'] = content
            elif title == 'Size':
                pi['size'] = int(content)
            elif title == 'Vendor':
                pi['vendor'] = content
            elif title == 'Packager':
                pi['packager'] = content
            elif title == 'Summary':
                pi['summary'] = content
            elif title == 'URL':
                pi['url'] = content
            else:
                continue
        pi['description'] = ''.join(package_desc)
        pi['files'] = files
        return pi

    def make_label(self, name, epoch, version, release):
        '''returns a label so that dnf can find the right package. arch and releasever are specified with flags, but release can be more specific'''
        label = name
        if epoch and epoch != 0:
            label += '-' + epoch + ':'
        else:
            label += '-'

        if version and release:
            return label + version + '-' + release
        elif version:
            return label + version
        else:
            return name

    def _build_params(self, arch, distro, repo_ids=None):
        '''return the params for yum downloader to use the right arch, distro, and releasever. TONS of yum peculiarities to work around'''
        cmd = ''
        if arch and arch != 'noarch':
            #important that noarch follows the specified arch
            if arch == 'i686':
                cmd += '--archlist=i386,i686,noarch '
            else:
                cmd += '--archlist=%s,noarch ' % arch
        else:
            cmd += '--archlist=noarch '

        cmd += '--releasever=%s ' % distro.split()[1]
        cmd += '--disablerepo=* '
        if repo_ids:
            repos_to_enable = repo_ids
        else:
            repos_to_enable = repos.get(distro, [])
        for repo in repos_to_enable:
            cmd += '--enablerepo=%s ' % repo
        return cmd

    #downloads a package with yumdownloader and returns the absolute path to it
    def download_package(self, label, arch, distro, package_list=None, repo_ids=None):
        '''downloads a package with yumdownloader and returns the absolute path to it. temp script is created because name of file downloaded is captured by script.'''

        #check to see if package already exists
        if not package_list: package_list = self.list_package(label, arch, distro, repo_ids)
        for p in package_list:
            package_path = temp_dir + p
            if os.path.isfile(package_path):
                return package_path

        self.logger.info("DownloadPackage: Downloading package with label %s" % label)
        script_temp = '%s.script.%s' % (temp_dir + label, int(random.random() * 1000))
        cmd = 'script %s -c \"yumdownloader -v --destdir=%s ' % (script_temp, temp_dir)
        params = self._build_params(arch, distro, repo_ids)

        cmd += params + label + '\"'
        proc = komand.helper.exec_command(cmd)
        if proc['rcode'] == 0 and proc['stderr'] == b'':
            #check to see if file was actually downloaded
            with open(script_temp, 'r', encoding='utf-8') as f:
                lines = [l.strip() for l in f.readlines()]
            for line in lines:
                if line == '':
                    continue
                else:
                    found_label = line.split(' ', 1)[0].strip()
                    if found_label.endswith('.rpm'):
                        os.remove(script_temp)
                        return temp_dir + found_label
            self.logger.error('DownloadPackage: ' + (proc['stdout'] + proc['stderr']).decode('utf-8'))
            os.remove(script_temp)
            raise Exception('DownloadPackage: Package unable to be downloaded.')
        else:
            self.logger.error('DownloadPackage: ' + (proc['stdout'] + proc['stderr']).decode('utf-8'))
            os.remove(script_temp)
            raise Exception('DownloadPackage: Package unable to be downloaded.')

    def _add_rpm_ext(self, p):
        if not p.endswith('.rpm'):
            return p + '.rpm'
        else:
            return p

    def _add_rpm_exts(self, packages):
        ps = []
        for p in packages:
            ps.append(self._add_rpm_ext(p))
        return ps

    def _format_repofile(self, r):
        return r if r.endswith('.repo') else r + '.repo'

    def _trim_epoch(self, p):
        '''trims epoch of 0 off of package'''
        if ':' in p and p[(p.index('-') + 1):p.index(':')] == '0':
            return p[:p.index('-') + 1] + p[(p.index(':') + 1):]
        else:
            return p

    def _trim_epochs(self, packages):
        '''trims epoch of 0 off of list of packages'''
        ps = []
        for p in packages:
            if ':' in p and p[(p.index('-') + 1):p.index(':')] == '0':
                ps.append(p[:p.index('-') + 1] + p[(p.index(':') + 1):])
            else:
                ps.append(p)
        return ps

    def list_package(self, label, arch, distro, repo_ids=None):
        '''return list of available packages (to find a name to check the cache)'''
        cmd = 'repoquery -q -a '

        params = self._build_params(arch, distro, repo_ids)
        cmd += params + label
        proc = komand.helper.exec_command(cmd)
        if proc['rcode'] != 0 or proc['stdout'] == '':
            self.logger.error('ListPackage: ' + (proc['stdout'] + proc['stderr']).decode('utf-8'))
            raise Exception("ListPackage: Package unable to be found with \'list\'")
        else:
            #fix this with decorators?
            package_list = self._add_rpm_exts(self._trim_epochs(proc['stdout'].decode('utf-8').splitlines()))
            return package_list

