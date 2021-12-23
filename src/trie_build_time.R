### filename = "../trie_build.csv"
filename = "../trie_build_aabb.csv"
### filename = "../trie_build_Kalevala.csv"

metadata  <- readLines(file(filename, encoding="UTF-8"), n=4)
metatext <- paste(gsub("# ", "", metadata), collapse="\n")

input <- read.table(filename,
                         dec=".",
                         quote="\"",
                         sep=";",
                         comment.char="#",
                         header=TRUE)

### buildtimes = input[input$generator == "Node class (Dictionary)",]
### buildtimes = input[input$generator == "Trie class (List)",]
buildtimes = input

shapes = c(16, 17)
shapes  <- shapes[factor(buildtimes$generator)]

plot(buildtimes$input_length,
     buildtimes$time,
     col=factor(buildtimes$depth),
     pch=shapes,
     xlab="Input text length (words)",
     ylab="Build time (s)",
     main="Trie tree build times")

legend("topleft",
       legend=levels(factor(buildtimes$depth)),
       col=factor(buildtimes$depth),
       pch=15,
       title="Depth")

legend("bottomright",
       legend=levels(factor(buildtimes$generator)),
       pch=c(16,17))       

text(25000, 0.25, metatext)
