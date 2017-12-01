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


--
-- Name: plpythonu; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: pi
--

CREATE OR REPLACE PROCEDURAL LANGUAGE plpythonu;


ALTER PROCEDURAL LANGUAGE plpythonu OWNER TO pi;

SET search_path = public, pg_catalog;

--
-- Name: ema_func(numeric, double precision, numeric); Type: FUNCTION; Schema: public; Owner: pi
--

CREATE FUNCTION ema_func(state numeric, inval double precision, alpha numeric) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
begin
  return case
         when state is null then inval
         else alpha * inval + (1-alpha) * state
         end;
end
$$;


ALTER FUNCTION public.ema_func(state numeric, inval double precision, alpha numeric) OWNER TO pi;

--
-- Name: ema(double precision, numeric); Type: AGGREGATE; Schema: public; Owner: pi
--

CREATE AGGREGATE ema(double precision, numeric) (
    SFUNC = ema_func,
    STYPE = numeric
);


ALTER AGGREGATE public.ema(double precision, numeric) OWNER TO pi;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: stock_hist; Type: TABLE; Schema: public; Owner: pi; Tablespace: 
--

CREATE TABLE stock_hist (
    dt date,
    ticker text,
    open double precision,
    close double precision,
    low double precision,
    high double precision,
    volume double precision
);


ALTER TABLE stock_hist OWNER TO pi;

--
-- Name: stock_w_ema; Type: VIEW; Schema: public; Owner: pi
--

CREATE VIEW stock_w_ema AS
SELECT stock_hist.dt,
    stock_hist.ticker,
    stock_hist.close,
    ema(stock_hist.close, 0.1818181818181818) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt) AS ema10,
    ema(stock_hist.close, 0.0952380952380952) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt) AS ema20,
    (avg((stock_hist.high-stock_hist.low)/2) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt ROWS BETWEEN 34 PRECEDING AND CURRENT ROW)
     - avg((stock_hist.high-stock_hist.low)/2) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt ROWS BETWEEN 5 PRECEDING AND CURRENT ROW)) AS ao,
   round((stock_hist.volume * (stock_hist.close - lag(stock_hist.close) OVER (PARTITION BY stock_hist.ticker ORDER BY stock_hist.dt)))) AS raw_fi,
   stock_hist.volume
   FROM stock_hist;

ALTER TABLE stock_w_ema OWNER TO pi;

drop view stock_w_fi;
create or replace view stock_w_fi as
select 
dt, ticker,
close,
lag(close) OVER (PARTITION BY ticker ORDER BY dt) as prev_close,
lag(close,7) OVER (PARTITION BY ticker ORDER BY dt) as week_ago_close,
ema10,
lag(ema10) OVER (PARTITION BY ticker ORDER BY dt) as prev_ema10,
ema20,
lag(ema20) OVER (PARTITION BY ticker ORDER BY dt) as prev_ema20,
ao,
lag(ao) OVER (PARTITION BY ticker ORDER BY dt) as prev_ao,
ema(raw_fi, 0.6666666666666667) OVER (PARTITION BY ticker ORDER BY dt) AS fi2,
ema(raw_fi, 0.1428571428571429) OVER (PARTITION BY ticker ORDER BY dt) AS fi13
from stock_w_ema;

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

