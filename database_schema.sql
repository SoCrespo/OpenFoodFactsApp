-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema openfoodfacts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `category` ;

CREATE TABLE IF NOT EXISTS `category` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT 'corresponds to categories field in OFF answer',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `product` ;

CREATE TABLE IF NOT EXISTS `product` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(50) NOT NULL COMMENT 'Corresponds to brands_tags',
  `name` VARCHAR(50) NOT NULL COMMENT 'Corresponds to product_name_fr',
  `full_name` VARCHAR(100) CHARACTER SET 'utf8' NULL COMMENT 'Corresponds to generic_name_fr',
  `nutriscore_index` CHAR(1) NOT NULL COMMENT 'corresponds to nutriscore_grades',
  `cat_id` INT(11) NOT NULL,
  `url` VARCHAR(2000) NOT NULL COMMENT 'corresponds to url',
  `ingredients` VARCHAR(2000) NULL COMMENT 'corresponds to ingredients_text',
  `stores` VARCHAR(50) NULL COMMENT 'Corresponds to stores',
  `quantity` VARCHAR(8) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_product_category` (`cat_id` ASC),
  INDEX `idx_prod_name` (`name` ASC),
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`cat_id`)
    REFERENCES `category` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `substitution`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `substitution` ;

CREATE TABLE IF NOT EXISTS `substitution` (
  `origin_id` INT NOT NULL,
  `substitute_id` INT NOT NULL,
  INDEX `fk_origin_product_idx` (`origin_id` ASC),
  INDEX `fk_substitute_product_idx` (`substitute_id` ASC),
  PRIMARY KEY (`origin_id`, `substitute_id`),
  CONSTRAINT `fk_origin_product`
    FOREIGN KEY (`origin_id`)
    REFERENCES `product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_substitute_product`
    FOREIGN KEY (`substitute_id`)
    REFERENCES `product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
