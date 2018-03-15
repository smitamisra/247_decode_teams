import os
import logging
import datetime
import json
import glob

logger = logging.getLogger()

for day_num in range(1, 32):
    path = os.path.join('/data/kinesis/', "{:02d}/*/*".format(day_num))
    day = datetime.date(year=2017, month=10, day=day_num)
    for idx, fname in enumerate(glob.iglob(path)):
        logger.info("{}: Working on {:,}".format(day, idx))
        with open(fname, "r") as f:
            contents = f.read().decode("utf-8")
        newsletter_traffic = []
        for bit in contents[1:-1].split('}{'):
            try:
                rec = json.loads("{" + bit + "}")
            except ValueError as e:
                logger.warning("BAD JSON")
                continue
