import argparse

from kdb_vault_tools.processors import Processor

parser = argparse.ArgumentParser(description='KDB to vault CLI')
parser.add_argument('-i', '--input', help='Input *.kdbx file path', required=True)
parser.add_argument('-p', '--password', help='kdb password', required=True)
parser.add_argument('-u', '--url', help='vault url', required=True)
parser.add_argument('-t', '--token', help='vault token', required=True)
parser.add_argument('-b', '--base', help='vault base namespace', required=True)


def main(ns: argparse.Namespace):
    vault_conf = {"url": ns.url, "token": ns.token}
    kdb_conf = {"filename": ns.input, "password": ns.password}

    processor = Processor(vault_settings=vault_conf, kdb_settings=kdb_conf)
    processor.write_vault(base_path=ns.base)


if __name__ == '__main__':
    """
    Namespace Example:
        base: '/sandbox/org/team/foo/'
        input: 'kdb_tmp/secrets-20190422.kdbx'
        password: 'superSecret'
        token :'myroot'
        url: 'http://localhost:1234'
    """
    args = parser.parse_args()
    main(args)
