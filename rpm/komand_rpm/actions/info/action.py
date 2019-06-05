import komand
from .schema import InfoInput, InfoOutput
# Custom imports below
import os
from komand_rpm.util.rpm_helpers import RPMHelper


class Info(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='info',
                description='Get information about a package',
                input=InfoInput(),
                output=InfoOutput())
        self.rpm_helper = RPMHelper(logger=self.logger)

    def run(self, params={}):
        name = params.get('name')
        epoch = params.get('epoch')
        version = params.get('version')
        release = params.get('release')
        arch = params.get('arch')
        distro = params.get('distro')
        repo = params.get('repo')
        key = params.get('key')

        # Param verification
        if distro == 'CentOS 7' and arch != 'x86_64':
            self.logger.error('Run: CentOS 7 only supports x86_64. This most likely will fail.')
        if epoch == '0':
            epoch = None
        # Params verified

        label = self.rpm_helper.make_label(name, epoch, version, release)

        # add the custom repo and key if they exist
        repo_dic = self.rpm_helper.add_repo(repo) if repo else None
        if key:
            self.rpm_helper.add_key(key)

        # check to see if cache has the package
        package_list = self.rpm_helper.list_package(label, arch, distro,
                                                repo_dic['ids']) if repo_dic else self.rpm_helper.list_package(label, arch,
                                                                                                           distro)

        cache_dic = self.rpm_helper.check_rpm_cache(package_list)
        if cache_dic:
            return cache_dic

        # else download the package, convert it into a dic, update cache, then delete
        package_path = self.rpm_helper.download_package(label, arch, distro, package_list,
                                                    repo_dic['ids']) if repo_dic else self.rpm_helper.download_package(
            label, arch, distro, package_list, None)
        if key:
            self.rpm_helper.checksig(package_path)
        info = self.rpm_helper.package_info(package_path)
        dic = self.rpm_helper.info2dic(info)
        self.rpm_helper.update_cache(dic, package_path[package_path.rfind('/') + 1:])
        os.remove(package_path)
        if repo_dic:
            os.remove(repo_dic['path'])
        return dic

    def test(self):
        # TODO: Implement test function
        return {}
