
import os, platform, subprocess, dotbot
from typing import List, Dict, Union

class Sops(dotbot.Plugin):
    _directive = "sops"

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive: str, data: Union[List, Dict]):
        if directive != self._directive:
            raise ValueError('sops cannot handle directive %s' % directive)
        success = True
        defaults = self._context.defaults().get(self._directive, {})
        if isinstance(data, Dict):
            data = [{key: data[key]} if bool(data[key]) else key
                    for key in data]
        for item in data:
            file = None

            if isinstance(item, Dict):
                file, options = list(item.items())[0]
                source = defaults.get("source", file+".sops")
                if options is not None:
                    source = options.get("source", source)
            try:
                command = ['sops -d', source]
                proc = subprocess.run([' '.join(command)],
                                      shell=True, check=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, encoding="utf-8")
                f = open(file, "w")
                f.write(proc.stdout)
                f.close()
                self._log.info("%s decrypted" % file)
            except Exception as e:
                self._log.error(e)
                success = False

        return success