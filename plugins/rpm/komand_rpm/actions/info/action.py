import insightconnect_plugin_runtime
from .schema import InfoInput, InfoOutput, Input, Output, Component

# Custom imports below
import os
from komand_rpm.util.rpm_helpers import RPMHelper


class Info(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="info",
            description=Component.DESCRIPTION,
            input=InfoInput(),
            output=InfoOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        name = params.get(Input.NAME, "")
        epoch = params.get(Input.EPOCH, "")
        version = params.get(Input.VERSION, "")
        release = params.get(Input.RELEASE, "")
        arch = params.get(Input.ARCH, "")
        distro = params.get(Input.DISTRO, "")
        repo = params.get(Input.REPO, "")
        key = params.get(Input.KEY, "")
        # END INPUT BINDING - DO NOT REMOVE

        helper = RPMHelper(logger=self.logger)

        # Validate user-supplied inputs
        for value, field in (
            (name, "name"),
            (epoch, "epoch"),
            (version, "version"),
            (release, "release"),
            (repo, "repo"),
            (key, "key"),
        ):
            if value:
                helper.validate_input(value, field)

        if repo:
            helper.validate_url(repo)
        if key:
            helper.validate_url(key)

        epoch = "" if epoch == "0" else epoch

        if distro == "CentOS 7" and arch != "x86_64":
            self.logger.error("CentOS 7 only supports x86_64 — this will likely fail")

        label = helper.make_label(name, epoch, version, release)
        self.logger.info(f"Run: Resolving package '{label}' [{arch}] on {distro}")

        repo_info = helper.add_repo(repo) if repo else None
        if key:
            helper.add_key(key)

        repo_ids = repo_info.get("ids") if repo_info else None
        package_list = helper.list_package(label, arch, distro, repo_ids)

        cached = helper.check_rpm_cache(package_list)
        if cached:
            self.logger.info("Run: Cache hit")
            return cached

        self.logger.info("Run: Cache miss — downloading")
        package_path = helper.download_package(label, arch, distro, package_list, repo_ids)
        try:
            if key:
                helper.checksig(package_path)
            info = helper.package_info(package_path)
            result = helper.info2dic(info)
            helper.update_cache(result, os.path.basename(package_path))
        finally:
            if os.path.isfile(package_path):
                os.remove(package_path)
            if repo_info and os.path.isfile(repo_info.get("path", "")):
                os.remove(repo_info.get("path"))

        self.logger.info(f"Run: Done — {result.get(Output.NAME, label)}")
        return result
