### filename = "../trie_build.csv"
filename = "../trie_build_aabb.csv"
### filename = "../trie_build_Kalevala.csv"

metadata  <- readLines(file(filename, encoding="UTF-8"), n=4)
metatext <- paste(gsub("# ", "", metadata), collapse="\n")

buildtimes <- read.table(filename,
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

text(25000, 0.23, buildtimes_metatext)
