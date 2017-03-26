NT <- read.csv(file ="/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/NTstatus.csv")
status <- NT[,1]
number <-NT[,2]
barplot(number,main="NT Status", xlab="Rate of Change", ylab= "Species", names.arg=status)

dput(number)
