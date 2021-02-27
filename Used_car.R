used_car <- read.csv("C:/Semester 2 university of southampton/COMP 6237 Data Mining/vehicles.csv",header = TRUE)

#Checking data type
str(used_car)
library(dplyr)
# Get rid of variables (image url, VIM, region URL, unnamed, id, url, model, size -seem similar average price)
used_car_clean <-used_car%>% select(region,price,year,manufacturer,condition,
                   cylinders,fuel,odometer,title_status,transmission,
                   drive,type,paint_color,state,posting_date)
str(used_car_clean)

#one hot encode (manufacturer, condition, type, cylinders, fuel, title status, transmission, drive, paint car)
used_car_clean$manufacturer <- as.factor(used_car_clean$manufacturer)
used_car_clean$condition <- as.factor(used_car_clean$condition)
used_car_clean$type <- as.factor(used_car_clean$type)
used_car_clean$cylinders <- as.factor(used_car_clean$cylinders)
used_car_clean$fuel <- as.factor(used_car_clean$fuel)
used_car_clean$title_status <- as.factor(used_car_clean$title_status)
used_car_clean$transmission <- as.factor(used_car_clean$transmission)
used_car_clean$drive <- as.factor(used_car_clean$drive)
used_car_clean$paint_color <- as.factor(used_car_clean$paint_color)
str(used_car_clean)
summary(used_car_clean)

# extract year and month post separately
used_car_clean$posting_year <- substring(used_car_clean$posting_date,1,4)
used_car_clean$posting_month <- substring(used_car_clean$posting_date,6,7)
summary(used_car_clean)
# get rid of posting date
used_car_clean <-used_car_clean%>% select(region,price,year,manufacturer,condition,
                                    cylinders,fuel,odometer,title_status,transmission,
                                    drive,type,paint_color,state,posting_year,posting_month)
str(used_car_clean)

# Converting posting year and posting month to num
used_car_clean$posting_month <- as.numeric(used_car_clean$posting_month)
used_car_clean$posting_year <- as.numeric(used_car_clean$posting_year)
summary(used_car_clean)

# Handling Price variable (get rid of missing value cars over 600,000)
summary(used_car_clean$price)
summary(is.na(used_car_clean$price))
# There is no missing data
# get rid of car over 600,000
used_car_clean_new <- used_car_clean[(used_car_clean$price <= 600000),]
summary(used_car_clean_new)
# remove price <= 600000 -> 458158
# Visualising each variable
library(ggplot2)

# manufacturer
# plot all manufacturers included NAN
plot_manufacturer <- ggplot(used_car_clean_new,aes(x = manufacturer, fill = manufacturer)) + geom_bar()
plot_manufacturer
summary(is.na(used_car_clean_new$manufacturer))
summary(used_car_clean_new$manufacturer)
# Drop row that manufacturer = ""
used_car_clean_new_drop_manu <- used_car_clean_new[!(used_car_clean_new$manufacturer == ""),]
summary(used_car_clean_new_drop_manu$manufacturer)
plot_manufacturer_1 <- ggplot(used_car_clean_new_drop_manu,aes(x = manufacturer, fill = manufacturer)) + geom_bar()
plot_manufacturer_1
# Drop Manufacturer -> 439944



# Consider variable condition
summary(used_car_clean_new_drop_manu$condition)
plot_condition <- ggplot(used_car_clean_new_drop_manu,aes(x = condition, fill = condition)) + geom_bar()
plot_condition
# Drop row that condition = ""
used_car_clean_new_drop_cond <- used_car_clean_new_drop_manu[!(used_car_clean_new_drop_manu$condition == ""),]
summary(used_car_clean_new_drop_cond$condition)
plot_condition_1 <- ggplot(used_car_clean_new_drop_cond,aes(x = condition, fill = condition)) + geom_bar()
plot_condition_1
# Drop condition -> 254833



# Consider variable condition
summary(used_car_clean_new_drop_cond$type)
plot_type <- ggplot(used_car_clean_new_drop_cond,aes(x = type, fill = type)) + geom_bar()
plot_type
# Drop row that type = "" | "other"
used_car_clean_new_drop_type <- used_car_clean_new_drop_cond[!(used_car_clean_new_drop_cond$type == "" ),]
# -> remain 218818
used_car_clean_new_drop_type <- used_car_clean_new_drop_type[!(used_car_clean_new_drop_type$type == "other" ),]
# -> remain 206037
summary(used_car_clean_new_drop_type$type)
plot_type_1 <- ggplot(used_car_clean_new_drop_type,aes(x = type, fill = type)) + geom_bar()
plot_type_1
