library(tidyverse)

output_dir <- '~/Dropbox/GlobalGits/reddit_fun/output/'

c1 <- read_csv(paste0(output_dir, '/train.csv'))
c2 <- read_csv(paste0(output_dir, '/spitout2.csv')) %>% filter(!is.na(comment))

big <- cbind(c1,c2)

ns <- names(big)

names(big)[5] <- "comment2"

wrong <- big %>% filter(subreddt_actual != subreddit)


# same but test


c1 <- read_csv(paste0(output_dir, '/test.csv'))
c2 <- read_csv(paste0(output_dir, '/spittest.csv')) %>% filter(!is.na(comment))

big <- cbind(c1,c2)

ns <- names(big)

names(big)[5] <- "comment2"


right <- big %>% filter(subreddt_actual == subreddit)
wrong <- big %>% filter(subreddt_actual != subreddit)
