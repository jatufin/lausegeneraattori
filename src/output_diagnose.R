### Run this after executing output_diagnose, to produce plots
### from the output file.
###
### Filename: output_diagnose.csv
###

#filename <- "../output_diagnose_aabb_Node.csv"
#filename <- "../output_diagnose_aabb_Trie.csv"
#filename <- "../output_diagnose_Kalevala_Node.csv"
filename <- "../output_diagnose_Kalevala_Node_long.csv"

metadata <- readLines(file(filename, encoding="UTF-8"), n=5)
metadata_text <- paste(gsub("# ", "", metadata), collapse="\n")

csv <- read.table(filename,
                  dec=".",
                  quote="\"",
                  sep=";",
                  comment.char="#",
                  header=TRUE)


plot(csv$number_of_sentences,
     csv$difference,
     col=factor(csv$degree),
     xlab="Number of generated sentences",
     ylab="Probability difference to original text",
     main="Probability for wollowing word")

text(25000, 0.20 ,metadata_text)

legend("topright",
       legend=levels(factor(csv$degree)),
       col=factor(csv$degree),
       pch=1,
       title="Preceeding words")

### plot(csv[csv$degree==3,]$number_of_sentences,csv[csv$degree==5,]$difference)
