#
# Home Control - Routes
# Created by Michael Abood on 10/19/24
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

import logging
from flask import Blueprint
route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/doorbell', methods=['POST'])
def hello_world():
    logging.info('Posted doorbell ring at %s', datetime.datetime.now())
    return "<p>Ring Ring</p>"
