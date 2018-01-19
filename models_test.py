# -*- coding: utf-8 -*-
import io
import sys
import json

import arrow

from app import db
from app.models import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def illegal_test():
    dev = Illegal.query.filter_by(ID='0C78CA51-CC0C-4D56-A55A-F324D0FFDE68').first()
    print(dev.VehicleNo)

if __name__ == '__main__':
    illegal_test()

