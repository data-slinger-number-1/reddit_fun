import random

output_dir = '~/Dropbox/GlobalGits/reddit_fun/'

with open('%s/output/comments.txt' % (output_dir), 'r') as f:
    all_shit = f.readlines()
    random.shuffle(all_shit)
    print(len(all_shit))
    split_point = int(.8 * len(all_shit))

    with open('%s/output/train.txt' % output_dir, 'w') as t:
        t.writelines(all_shit[0:split_point])
    with open('%s/output/test.txt' % output_dir, 'w') as t:
        t.writelines(all_shit[split_point:])
