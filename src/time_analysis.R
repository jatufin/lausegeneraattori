buildtimes_filename = "../trie_build.csv"
sentencegeneration_filename = "../sentence_generation.csv"

buildtimes_metadata  <- readLines(file(buildtimes_filename, encoding="UTF-8"), n=4)
buildtimes_metatext <- paste(gsub("# ", "", buildtimes_metadata), collapse="\n")

buildtimes <- read.table(buildtimes_filename,
                         dec=".",
                         quote="\"",
                         sep=";",
                         comment.char="#",
                         header=TRUE)

shapes = c(16, 17)
shapes  <- shapes[factor(buildtimes$generator)]

plot(buildtimes$input_length,
     buildtimes$time,
     col=factor(buildtimes$depth),
     pch=shapes,
     xlab="Input text length in words",
     ylab="Build time",
     main="Trie tree build times")

legend("topleft",
       legend=levels(factor(buildtimes$depth)),
       col=factor(buildtimes$depth),
       pch=15,
       title="Depth")

legend("bottomright",
       legend=levels(factor(buildtimes$generator)),
       pch=c(16,17))       

text(25000, 0.25, buildtimes_metatext)
