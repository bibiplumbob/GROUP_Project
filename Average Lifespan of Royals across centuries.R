library(tidyverse)
final_royal <- read_csv('final_royal.csv')

lifespan <- final_royal|>
  select(title,`ontology/birthYear`,`ontology/deathYear`)|>
  rename(birthyear = `ontology/birthYear`, deathyear = `ontology/deathYear`)|>
  na.omit()|>
  filter(birthyear >= 0, deathyear >=0)|>
  filter(deathyear > birthyear)

life_mutated <- lifespan |> 
  mutate(life = deathyear - birthyear)|>
  filter(life < 700) |>
  mutate(century = ceiling(birthyear / 100))
  
#PART2: calculating average life span according to different time periods
grouped_by_century <- life_mutated |>
  group_by(century) |>
  summarise(avg_lifespan = mean(life))


#PART3: Plot
line_plot <- ggplot(data = grouped_by_century)+
  aes (x = century, y = avg_lifespan)+
  geom_line()+
  theme_grey()+
  ylim(c(0,80))


line_plot <- line_plot + labs (title = 'Average Lifespan of Royals Across Centuries',
                                     x = 'Centuries',
                                     y = 'Average Life Span')

print(line_plot)

  
