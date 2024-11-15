CREATE TABLE `users` (
    `id` MEDIUMINT AUTO_INCREMENT,
    `follower_id` MEDIUMINT UNSIGNED,
    `first_name` VARCHAR(32) NOT NULL,
    `last_name` VARCHAR(32) NOT NULL,
    `username` VARCHAR(32) NOT NULL UNIQUE,
    `password` VARCHAR(32) NOT NULL,
    `school_start_date` DATETIME NOT NULL,
    `school_end_date` DATETIME NOT NULL,
    `title` VARCHAR(32),
    `work_start_date` DATETIME,
    `work_end_date` DATETIME,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`follower_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `schools` (
    `id` MEDIUMINT AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL UNIQUE,
    `user_id` MEDIUMINT UNSIGNED,
    `type` ENUM("Primary", "Secondary", "Higher Education"),
    `location` TEXT,
    `year_founded` YEAR(4) CHECK(`year_founded` > 0),
    `school_start_date` DATETIME NOT NULL,
    `school_end_date` DATETIME NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `companies` (
    `id` MEDIUMINT AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL UNIQUE,
    `industry` ENUM("Technology", "Education", "Business"),
    `location` VARCHAR(32),
    `user_id` MEDIUMINT UNSIGNED,
    `title` VARCHAR(32),
    `work_start_date` DATETIME,
    `work_end_date` DATETIME,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);