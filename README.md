[dotbot_repo]: https://github.com/anishathalye/dotbot

## Dotbot ```sops``` Plugin

Plugin for [Dotbot][dotbot_repo], that adds ```sops``` directive, which allows you to decrypt files encrypted with sops.

## Installation

1. Simply add this repo as a submodule of your dotfiles repository:
```
git submodule add https://github.com/elogiclab/dotbot-sops.git
```

2. Pass this folder (or directly sops.py file) path with corresponding flag to your [Dotbot][dotbot_repo] script:
- ```-p /path/to/file/sops.py```

or

- ```--plugin-dir /pato/to/plugin/folder```

## Usage

### Example config
```yaml
- sops:
    systemd/cryfs.conf:
      source: systemd/cryfs.sops.conf
```
You need to have sops installed and the .sops.yaml file present in the directory where the encrypted file is located.

Typically you will have the encrypted file committed to the repository and the plaintext file specified in the .gitignore. Place the sops directive before the linking process so that you will have the decrypted file ready to be linked.

For more information on how to encrypt files with sops refer to the sops documentation. [This is a practical example](https://blog.gitguardian.com/a-comprehensive-guide-to-sops/) of how to encrypt a file using gpg.