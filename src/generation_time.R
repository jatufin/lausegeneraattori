### filename = "../sentence_generation.csv"
### filename = "../sentence_generation_aabb.csv"
filename = "../sentence_generation_Kalevala.csv"


metadata  <- readLines(file(filename, encoding="UTF-8"), n=4)
metatext <- paste(gsub("# ", "", metadata), collapse="\n")

generation <- read.table(filename,
                         dec=".",
                         quote="\"",
                         sep=";",
                         comment.char="#",
                         header=TRUE)

shapes = c(16, 17)
shapes  <- shapes[factor(generation$generator)]

plot(generation$sentence_length,
     generation$speed,
     col=factor(generation$markov_degree),
     pch=shapes,
     xlab="Generated sentence length",
     ylab="Generation speed",
     main="Sentence generation speed")

legend("topleft",
       legend=levels(factor(generation$markov_degree)),
       col=factor(generation$markov_degree),
       pch=15,
       title="Depth")

legend("topright",
       legend=levels(factor(generation$generator)),
       pch=c(16,17))       

text(13, 100000, buildtimes_metatext)
