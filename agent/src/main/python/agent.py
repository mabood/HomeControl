#
# Home Control - Agent
# Created by Michael Abood on 04/19/20
#
#    This file is part of Home Control.
#
#    Home Control is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Home Control is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Home Control.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import os
import logging
import utils
import constants
from sensors import SensorManager
from services import ServiceManager
from configparser import ConfigParser


def agent_main():
    # Resolve homecontrol root directory absolute path
    root_directory = os.getenv(constants.HOMECONTROL_ROOT_ENVIRONMENT_VAR)
    if not root_directory or not os.path.isdir(root_directory):
        print('Unable to resolve homecontrol root directory from environment variables. Use launch.sh to run agent')
        sys.exit(1)

    # Setup logging
    log_directory = os.getenv(constants.AGENT_RUN_DIR_ENVIRONMENT_VAR)
    if not log_directory or not os.path.isdir(log_directory):
        print('Unable to resolve agent run directory from environment variables')
        sys.exit(1)

    utils.setup_logger(constants.AGENT_APP_NAME, log_directory)

    # Setup config
    agent_config_file = os.path.join(root_directory, constants.AGENT_CONFIG_PATH)
    if not agent_config_file or not os.path.isfile(agent_config_file):
        logging.error('Failed to resolve agent config file at relative path %s' % constants.AGENT_CONFIG_PATH)
        sys.exit(2)

    config = ConfigParser()
    config.read(agent_config_file)

    # Start sensor data collection
    sensors = SensorManager(config)
    sensors.start_collection()

    # Start agent services
    services = ServiceManager(config)
    services.start_services()


if __name__ == '__main__':
    agent_main()
