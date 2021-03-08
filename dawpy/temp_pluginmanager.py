import os
import urllib.request
import zipfile


class PluginManager:
    def ensure(self, url: str, folder: str):
        """ ensures, that the target file of the url is present in the given folder """
        name = url.rsplit("/", 1)[-1]
        filename = os.path.join(folder, name)
        if not os.path.isfile(filename):
            print("Downloading: " + filename)
            try:
                urllib.request.urlretrieve(url, filename)
                return True
            except Exception as inst:
                print(inst)
                print("  Encountered unknown error. Continuing.")
                return False

    def enshureUnZipped(self, url: str, folder: str):
        name = url.rsplit("/", 1)[-1]
        filename = os.path.join(folder, name)
        ret = self.ensure(url, folder)

        if ret and zipfile.is_zipfile(filename):
            with zipfile.ZipFile(filename) as myzip:
                myzip.extractall()
