library(tidyverse)

final_royal <- read_csv('final_royal.csv')

lifespan <- final_royal|>
  select(title,`ontology/birthYear`,`ontology/deathYear`,num_spouses)|>
  rename(birthyear = `ontology/birthYear`, deathyear = `ontology/deathYear`)|>
  na.omit()|>
  filter(num_spouses <= 3)|>
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


# #PART3: Average Plot
# line_plot <- ggplot(data = grouped_by_century)+
#   aes (x = century, y = avg_lifespan)+
#   geom_line()+
#   theme_grey()+
#   ylim(c(0,80))+
#   xlim(c(9, 20))
# 
# 
# line_plot <- line_plot + labs (title = 'Average Lifespan of Royals Across Centuries',
#                                x = 'Centuries',
#                                y = 'Average Life Span')
# 
# print(line_plot)

# #PART4: Scatter Plot
# scatter_plot <- ggplot(data = life_mutated)+
#   aes(x = birthyear, y = life, color = as.factor(num_spouses)) +
#   geom_point()+
#   theme_grey(base_family = "sans")+
#   ylim(c(0,110))+
#   xlim(c(1000, 2000))+
#   geom_line(data = grouped_by_century, mapping = aes(y=avg_lifespan, x = century *100), size=1.2, color = "#1B762E")
# 
# scatter_plot <- scatter_plot + labs (title = 'Lifespan of Royals during A.D. 1000-2000',
#                                      x = 'Birth Year',
#                                      y = 'Life Span',
#                                      color = "Number of Spouses")
# 
# print(scatter_plot)


#MY PART

# Reading in the the file and renaming the annoying variable names

life_expectancy <- read_csv("life-expectancy.csv") |>
  rename(life_expectancy = `Life expectancy at birth (historical)`)

# Creating the varaible with average life expectancy for each year (mean of life expectacies for each country in a given year)

life_expectancy |>
  mutate(century = ceiling(Year/100))|>
  group_by(century) |>
  summarise(avg_life_expectancy = mean(life_expectancy))-> data_for_figure

# Creating a figure with it (Contains the Avg life expectancy for nobles and overa)

read_csv("noble_life.csv")|>
  mutate(century = (year/100))|>
  group_by(century) -> noble_file


line_figure <- ggplot() +
  aes(x = century*100)+
  geom_line(data = data_for_figure, aes(y = avg_life_expectancy), color = "#1B762E", size=1.2)+
  geom_line(data = grouped_by_century, aes(y = avg_lifespan), color = "#DF3B3B", size=1.2)+
  geom_line(data = noble_file, aes(y=noble_life_expectancy), color= "#3B88DF", size=1.2)+
  xlim(c(1000, 2000))+
  labs(title = 'Lifespan of Various Social Groups 1000-2000 AD',
                                                x = 'Birth Year',
                                                y = 'Life Span')


print(line_figure)          