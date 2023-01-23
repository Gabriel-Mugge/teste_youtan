-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema youtan_jr
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema youtan_jr
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `youtan_jr` DEFAULT CHARACTER SET utf8 ;
USE `youtan_jr` ;

-- -----------------------------------------------------
-- Table `youtan_jr`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `youtan_jr`.`Empresa` (
  `cnpj_empresa` VARCHAR(20) NOT NULL,
  `nome_empresa` VARCHAR(45) NULL,
  `situacao_empresa` VARCHAR(45) NULL,
  PRIMARY KEY (`cnpj_empresa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `youtan_jr`.`Filial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `youtan_jr`.`Filial` (
  `id_filial` INT NOT NULL AUTO_INCREMENT,
  `nome_filial` VARCHAR(45) NULL,
  `situacao_filial` VARCHAR(45) NULL,
  `Empresa_cnpj_empresa` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id_filial`, `Empresa_cnpj_empresa`),
  INDEX `fk_Filial_Empresa_idx` (`Empresa_cnpj_empresa` ASC),
  CONSTRAINT `fk_Filial_Empresa`
    FOREIGN KEY (`Empresa_cnpj_empresa`)
    REFERENCES `youtan_jr`.`Empresa` (`cnpj_empresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `youtan_jr`.`Admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `youtan_jr`.`Admin` (
  `id_admin` INT NOT NULL AUTO_INCREMENT,
  `usuario_admin` VARCHAR(45) NULL,
  `senha_admin` VARCHAR(45) NULL,
  PRIMARY KEY (`id_admin`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
