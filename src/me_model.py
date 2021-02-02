import fasttext
import re
import csv

project_dir = '~/Dropbox/GlobalGits/reddit_fun/'

def do_modeling(model_name, input, epoch, lr, wordNgrams):
    model = fasttext.train_supervised(input=input, lr=lr, epoch=epoch, wordNgrams=wordNgrams)
    model.save_model("%s.bin" % (model_name))

# actually see how the predictions shake out

if __name__ == "__main__":
    model = fasttext.load_model("%s/output/bloomingmodel.bin" % (project_dir))
    # check for 'overfitting' to train set.
    with open('%s/output/train_clean.txt' % (project_dir), 'r') as f:
        stuff = f.read()

    things = re.split("__label__\\w+",  stuff)

    with open('%s/output/spitout2.csv' % (project_dir), "w") as spit:
        csv_writer = csv.writer(spit)
        csv_writer.writerow(['subreddit', 'score', 'comment'])
        for thing in things:
            thing = thing.replace("\n","")
            print(thing)
            res = model.predict(thing)
            #spit.write("%s,%s,%s\n"  %
            csv_writer.writerow([res[0][0], res[1][0], thing])