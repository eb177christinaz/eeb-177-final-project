library(ggplot2)

setwd("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera")
chiroptera <- read.csv("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/chiropteragenusspeciesints.csv", header = F, as.is = T)
names(chiroptera) <- c("genus", "species", "minage", "maxage")
head(chiroptera)

library(forcats)
library(tidyr)
library(dplyr)

chiroptera_occ <- ggplot(chiroptera_occ, aes( x = species, maxage, colour = genus))

chiroptera_occ + geom_linerange(aes(ymin = minage, ymax = maxage)) + theme(legend.position="none") +  coord_flip() +  theme(axis.text.y = element_text(size=3)) + scale_y_continuous(limits=c(0, 50), expand = c(0, 0), breaks=c(0, 10, 20, 30, 40, 50)) + labs(title = "Chiroptera Fossil Occurrences", x = "Species", y = "Million Years Ago") + theme(plot.title = element_text(hjust = 0.5, size=22, face = "bold"), axis.title =element_text(size=20)) 

chiroptera_occ <- ggplot(chiroptera, aes( x = fct_reorder(species, minage, .desc = T), maxage, colour = genus))

chiroptera_occ + geom_linerange(aes(ymin = minage, ymax = maxage + 0.5)) + theme(legend.position="none") +  coord_flip() +  theme(axis.text.y = element_text(size=3)) + scale_y_continuous(limits=c(0, 50), expand = c(0, 0), breaks=c(0, 10, 20, 30, 40, 50)) + labs(title = "Chiroptera Fossil Occurrences", x = "Species", y = "Ma ago") + theme(plot.title = element_text(hjust = 0.5, size=22, face = "bold"), axis.title =element_text(size=20)) 

diversity <- chiroptera %>% gather(key = type, value = age, minage, maxage) %>% mutate(count = ifelse(type == "maxage", 1, -1)) %>% group_by(age) %>% summarise(count = sum(count))  %>% arrange(-age, -count) %>% mutate(diversity = cumsum(count))

ggplot(diversity, aes(x = age, y = diversity)) + geom_step()
