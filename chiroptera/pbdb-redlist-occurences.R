setwd("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera")
chiroptera <- read.csv("/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/alldatamatches.csv", header = F, as.is = T)
species <- chiroptera[,4]
maxage <- chiroptera[,9]
minage <- chiroptera[,10]
head(chiroptera)

chiroptera_occ <- ggplot(chiroptera, aes( x = species, maxage, colour = species))

chiroptera_occ + geom_linerange(aes(ymin = minage, ymax = maxage)) + theme(legend.position="none") +  coord_flip() +  theme(axis.text.y = element_text(size=3)) + scale_y_continuous(limits=c(0, 50), expand = c(0, 0), breaks=c(0, 10, 20, 30, 40, 50)) + labs(title = "Canid Fossil Occurrences", x = "Species", y = "Million Years Ago") + theme(plot.title = element_text(hjust = 0.5, size=22, face = "bold"), axis.title =element_text(size=20)) 

#chiroptera_occ <- ggplot(chiroptera, aes( x = fct_reorder(species, minage, .desc = T), maxage, colour = genus))

#chiroptera_occ + geom_linerange(aes(ymin = minage, ymax = maxage + 0.5)) + theme(legend.position="none") +  coord_flip() +  theme(axis.text.y = element_text(size=3)) + scale_y_continuous(limits=c(0, 50), expand = c(0, 0), breaks=c(0, 10, 20, 30, 40, 50)) + labs(title = "Canid Fossil Occurrences", x = "Species", y = "Million Years Ago") + theme(plot.title = element_text(hjust = 0.5, size=22, face = "bold"), axis.title =element_text(size=20)) 