import asyncio
import argparse
from auth.cli import register_commands as register_auth_commands

async def test(_):
    print("Test message")

parser = argparse.ArgumentParser(description="CLI commands")
subparsers = parser.add_subparsers(dest="command", required=True, )


parser_test = subparsers.add_parser('test', help="Print test message")
parser_test.set_defaults(func=test)

register_auth_commands(subparsers)
