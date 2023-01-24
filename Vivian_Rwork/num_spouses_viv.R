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
n_spouse_scatter <- royals_age |>
  filter(!is.na(num_spouses))|>
  ggplot()+
  aes(x = num_spouses, y = lifespan)+
  geom_point()+
  labs(title = "Impact of number of spouses on the lifespan of royalty")+
  xlab("Number of spouses")+
  ylab("Lifespan in Years")

print(n_spouse_scatter)