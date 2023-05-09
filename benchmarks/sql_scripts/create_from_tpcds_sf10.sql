create schema IF NOT EXISTS hive.tpcds10;

create table IF NOT EXISTS hive.tpcds10.call_center as SELECT * FROM tpcds.sf10.call_center limit 0;
create table IF NOT EXISTS hive.tpcds10.catalog_page as SELECT * FROM tpcds.sf10.catalog_page limit 0;
create table IF NOT EXISTS hive.tpcds10.catalog_returns as SELECT * FROM tpcds.sf10.catalog_returns limit 0;
create table IF NOT EXISTS hive.tpcds10.catalog_sales as SELECT * FROM tpcds.sf10.catalog_sales limit 0;
create table IF NOT EXISTS hive.tpcds10.customer as SELECT * FROM tpcds.sf10.customer limit 0;
create table IF NOT EXISTS hive.tpcds10.customer_address as SELECT * FROM tpcds.sf10.customer_address limit 0;
create table IF NOT EXISTS hive.tpcds10.customer_demographics as SELECT * FROM tpcds.sf10.customer_demographics limit 0;
create table IF NOT EXISTS hive.tpcds10.date_dim as SELECT * FROM tpcds.sf10.date_dim limit 0;
--create table IF NOT EXISTS hive.tpcds10.dbgen_version as SELECT * FROM tpcds.sf10.dbgen_version limit 0;
create table IF NOT EXISTS hive.tpcds10.household_demographics as SELECT * FROM tpcds.sf10.household_demographics limit 0;
create table IF NOT EXISTS hive.tpcds10.income_band as SELECT * FROM tpcds.sf10.income_band limit 0;
create table IF NOT EXISTS hive.tpcds10.inventory as SELECT * FROM tpcds.sf10.inventory limit 0;
create table IF NOT EXISTS hive.tpcds10.item as SELECT * FROM tpcds.sf10.item limit 0;
create table IF NOT EXISTS hive.tpcds10.promotion as SELECT * FROM tpcds.sf10.promotion limit 0;
create table IF NOT EXISTS hive.tpcds10.reason as SELECT * FROM tpcds.sf10.reason limit 0;
create table IF NOT EXISTS hive.tpcds10.ship_mode as SELECT * FROM tpcds.sf10.ship_mode limit 0;
create table IF NOT EXISTS hive.tpcds10.store as SELECT * FROM tpcds.sf10.store limit 0;
create table IF NOT EXISTS hive.tpcds10.store_returns as SELECT * FROM tpcds.sf10.store_returns limit 0;
create table IF NOT EXISTS hive.tpcds10.store_sales as SELECT * FROM tpcds.sf10.store_sales limit 0;
create table IF NOT EXISTS hive.tpcds10.time_dim as SELECT * FROM tpcds.sf10.time_dim limit 0;
create table IF NOT EXISTS hive.tpcds10.warehouse as SELECT * FROM tpcds.sf10.warehouse limit 0;
create table IF NOT EXISTS hive.tpcds10.web_page as SELECT * FROM tpcds.sf10.web_page limit 0;
create table IF NOT EXISTS hive.tpcds10.web_returns as SELECT * FROM tpcds.sf10.web_returns limit 0;
create table IF NOT EXISTS hive.tpcds10.web_sales as SELECT * FROM tpcds.sf10.web_sales limit 0;
create table IF NOT EXISTS hive.tpcds10.web_site as SELECT * FROM tpcds.sf10.web_site limit 0;

