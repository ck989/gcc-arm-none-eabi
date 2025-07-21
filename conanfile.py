import os
from conan.tools.files import copy
from conan import ConanFile

class Package(ConanFile):
    name = "gcc-arm-none-eabi"
    version = "13.3.0"

    def build(self):
        url = "https://github.com/ck989/gcc-arm-none-eabi.git"
        self.run(f"git clone --depth=1 {url} gcc")
        return
    
    def package(self):
        copy(self, pattern="*", dst=self.package_folder, src=os.path.join(self.source_folder, "gcc"))
        return
    
    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        return

