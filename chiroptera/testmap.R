library(ggplot2)
setwd("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera")
bats <- read.csv("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/newchiropteragenusspecies-age.csv", header = F, as.is = T)
names(bats) <- c("genus","species", "maxage", "minage")
head(bats)

bat_occ <- ggplot(bats, aes( x = species, maxage, colour = genus))
# everything
bat_occ + geom_linerange(aes(ymin = minage, ymax = maxage + 0.5)) + theme(legend.position="none") +  coord_flip() +  theme(axis.text.y = element_text(size=1)) + scale_y_continuous(limits=c(0, 50), expand = c(0, 0), breaks=c(0, 10, 20, 30, 40, 50)) + labs(title = "Bat Fossil Occurrences", x = "Species", y = "Million Years ago") + theme(plot.title = element_text(hjust = 0.5, size=22, face = "bold"), axis.title =element_text(size=20)) 
