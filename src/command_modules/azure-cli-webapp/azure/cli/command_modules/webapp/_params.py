#pylint: disable=unused-import
import argparse

from azure.cli.commands import CliArgumentType, register_cli_argument

from azure.mgmt.web import WebSiteManagementClient
from azure.cli.commands.client_factory import get_mgmt_service_client

# FACTORIES

def _web_client_factory(**_):
    return get_mgmt_service_client(WebSiteManagementClient)

# PARAMETER REGISTRATIOn

register_cli_argument('webapp', 'name', CliArgumentType(options_list=('--name', '-n')))
