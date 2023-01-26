library(tidyverse)
library(ggthemes)


royal_data = read_csv("final_royal.csv")

#renaming columns
royal_data <- royal_data |>
  rename('title_label' = 'ontology/title', 
         'birthYear' = 'ontology/birthYear', 'deathYear' = 'ontology/deathYear')|>
  filter(deathYear > birthYear)

#Calculating age 

royals_age <- royal_data |>
  mutate(lifespan = deathYear - birthYear )|>
  filter(lifespan < 700)

#filtering spouse vs lifespan
violin_plot <- royals_age |>
  filter(!is.na(num_spouses))|>
  filter(num_spouses <= 3)|>
  ggplot()+
  aes(x = as.factor(num_spouses), y = lifespan)+
  geom_violin(fill = "#B3DAF1",
              show.legend = FALSE)+
  theme(text = element_text(family = "sans"))+
  labs(title = "Impact of number of spouses on the lifespan of royalty")+
  xlab("Number of spouses")+
  ylab("Lifespan in Years")+
  geom_boxplot(width = 0.1)

print(violin_plot)

ggsave("spouse_lifespan_violin.pdf")