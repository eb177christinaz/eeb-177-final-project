library(ggplot2)
library(ggmap)
library(maps)
library(mapdata)

batlocation <- read.csv(file = "/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/ONLYlocations.csv")[ ,c('lng','lat')]
longitude <- batlocation$lng 
latitude <- batlocation$lat

#Using GGPLOT, plot the Base World Map
mp <- NULL
mapWorld <- borders("world", colour="gray50", fill="gray50") # create a layer of borders
mp <- ggplot() +   mapWorld

#Now Layer the fossil records on top
mp <- mp+ geom_point(aes(x=longitude, y=latitude) ,color="blue", size=3) 
mp
