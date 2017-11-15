--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: stock_hist; Type: TABLE; Schema: public; Owner: pi; Tablespace: 
--

CREATE TABLE stock_hist (
    dt date,
    ticker text,
    close double precision,
    volume double precision
);


ALTER TABLE stock_hist OWNER TO pi;

--
-- Name: sber_w_ma; Type: VIEW; Schema: public; Owner: pi
--

CREATE VIEW sber_w_ma AS
 SELECT stock_hist.dt,
    stock_hist.close,
    avg(stock_hist.close) OVER (ORDER BY stock_hist.dt ROWS BETWEEN 10 PRECEDING AND CURRENT ROW) AS ma10,
    avg(stock_hist.close) OVER (ORDER BY stock_hist.dt ROWS BETWEEN 20 PRECEDING AND CURRENT ROW) AS ma20
   FROM stock_hist
  WHERE (stock_hist.ticker = 'SBER'::text);


ALTER TABLE sber_w_ma OWNER TO pi;

--
-- Name: stock_w_ma; Type: VIEW; Schema: public; Owner: pi
--

CREATE VIEW stock_w_ma AS
 SELECT stock_hist.dt,
    stock_hist.ticker,
    stock_hist.close,
    avg(stock_hist.close) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt ROWS BETWEEN 10 PRECEDING AND CURRENT ROW) AS ma10,
    avg(stock_hist.close) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt ROWS BETWEEN 20 PRECEDING AND CURRENT ROW) AS ma20,
    stock_hist.volume
   FROM stock_hist;


ALTER TABLE stock_w_ma OWNER TO pi;

--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

