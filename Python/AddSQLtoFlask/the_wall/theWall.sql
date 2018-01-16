-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema the_wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema the_wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `the_wall` DEFAULT CHARACTER SET utf8 ;
USE `the_wall` ;

-- -----------------------------------------------------
-- Table `the_wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(45) NULL,
  `date_created` DATETIME NULL,
  `date_updated` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `the_wall`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post` VARCHAR(255) NULL,
  `date_created` DATETIME NULL,
  `date_updated` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`users_id` ASC),
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `the_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `the_wall`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(255) NULL,
  `date_created` DATETIME NULL,
  `date_updated` DATETIME NULL,
  `users_id` INT NOT NULL,
  `posts_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`users_id` ASC),
  INDEX `fk_comments_posts1_idx` (`posts_id` ASC),
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `the_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`posts_id`)
    REFERENCES `the_wall`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
