VUEN <- read.csv(file ="/home/eeb177-student/Desktop/eeb-177/final-project/chiroptera/VUENstatus.csv")
status <- VUEN[,1]
number <-VUEN[,2]
barplot(number,main="VU-EN Status", xlab="Rate of Change", ylab= "Species", names.arg=status)

dput(number)
