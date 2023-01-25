library(tidyverse)

royals <- read_csv('final_royal.csv')

# Part 1 - finding lifespan
royals_year <- royals |>
  rename(death = `ontology/deathYear`, birth = `ontology/birthYear`)|>
  filter(birth >=0, death >=0) |>
  filter(death > birth) |>
  mutate(lifespan = death - birth)|>
  filter(lifespan < 700)

#lifespan_plot <- ggplot(data = royals_year) +
#  aes(x = title, y = lifespan)+
#  geom_col()+
#  theme_light()

#lifespan_plot <- lifespan_plot + labs(title = '...',
#                                            x = 'Name of Individual',
#                                            y = 'Lifespan')


# Part 2 - grouping the time period
