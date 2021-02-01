# fix it up some

import fasttext
import re
import csv

reg = re.compile('(__label__\S+) (.*)')

project_dir = '/Users/scharlesworth/Dropbox/GlobalGits/reddit_fun/'

with open('%s/output/train_clean.txt' % (project_dir), 'r') as f:
        stuff = f.readlines()


with open('%s/output/train.csv' % (project_dir), "w") as train:
        csv_writer = csv.writer(train)

        csv_writer.writerow(['subreddt_actual', 'comment'])

        for line in stuff:
            mt = reg.match(line)
            csv_writer.writerow([mt[1], mt[2]])
