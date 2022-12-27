library(xlsx)

#THIS IS FOR INDIVIDUALS (480)
df <- read.xlsx("dataF.xlsx", sheetIndex = 1)
df <- na.omit(df)

#THIS IS FOR COVERS (353)
#df <- read.csv("output.csv")

summary(df)

#CODE SET TO MODIFIED EVERY TIME
#df_s <- subset(df, Facial.Expression == "Confident")
#df <- df_s

# Print the data frame with sub-columns
print(df)


#PERCENTAGE TRANSFER
library(dplyr)

df <- df %>% 
  group_by(Title) %>% # Variable to be transformed
  count() %>% 
  ungroup() %>% 
  mutate(perc = `n` / sum(`n`)) %>% 
  arrange(perc) %>%
  mutate(labels = scales::percent(perc))


#BAR GGPLOT
library(ggplot2)

ggplot(df, aes(x = Title , y = perc, fill= Title)) +
  geom_col() +
  geom_text(aes(label = labels),
            position = position_stack(vjust = 0.5)) +
  guides(fill = guide_legend(title = "Shots")) +  
  labs(title = "Data Statistics")
