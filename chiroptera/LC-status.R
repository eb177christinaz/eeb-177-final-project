LC <- read.csv(file ="/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/LCstatus.csv")
status <- LC[,1]
number <-LC[,2]
barplot(number,main="LC Status", xlab="Rate of Change", ylab= "Species", names.arg=status)

dput(number)

