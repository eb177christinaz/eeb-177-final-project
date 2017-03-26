matchedendangered <- read.csv(file ="/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/PBDBendangerednumber.csv")
status <- matchedendangered[,1]
number <-matchedendangered[,2]
barplot(number,main="PBDB Bats Endangered Status", xlab="Endangered Status", ylab= "Number of fossils", names.arg=status)

dput(number)

