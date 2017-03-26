redlistendangered <- read.csv(file ="/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/redlistendangeredcount.csv")
redliststatus <- c("LC","NT","VU","EN","CR","EW","EX","DD")
redlistnumber <-redlistendangered[,2]
barplot(redlistnumber,main="Red List Bat Endangered Status", xlab="Endangered Status", ylab= "Number of fossils", names.arg=redliststatus)
      
dput(redliststatus)
        