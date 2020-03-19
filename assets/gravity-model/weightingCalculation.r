install.packages("MASS")
library(MASS)


gravityModelData <- read.csv("VagrantsExampleData.csv")

gravityModel <- glm.nb(vagrants~log(population)+log(distance)+wheat+wages+wageTrajectory, data=gravityModelData)
summary(gravityModel)
