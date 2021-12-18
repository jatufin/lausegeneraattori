library(ggplot2)

csv <- read.table("output_diagnose.csv", dec=".", sep=";", header=TRUE)



plot(csv$number_of_sentences,csv$difference)
plot(csv[csv$degree==3,]$number_of_sentences,csv[csv$degree==5,]$difference)
