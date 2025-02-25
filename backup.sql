--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: driver; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.driver (
    id uuid NOT NULL,
    name character varying NOT NULL,
    last_location public.geometry(Point,4326),
    fcm_token character varying,
    surname character varying NOT NULL
);


--
-- Name: rideoffer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rideoffer (
    id uuid NOT NULL,
    "time" double precision NOT NULL,
    distance double precision NOT NULL,
    start_location public.geometry(Point,4326),
    end_location public.geometry(Point,4326),
    price double precision NOT NULL,
    confirmed boolean NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    driver_id uuid NOT NULL
);


--
-- Name: user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."user" (
    id uuid NOT NULL,
    name character varying NOT NULL,
    surname character varying NOT NULL
);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alembic_version (version_num) FROM stdin;
951847d038cc
\.


--
-- Data for Name: driver; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.driver (id, name, last_location, fcm_token, surname) FROM stdin;
1ed651d5-a54f-402d-8569-5b1ac2495278	John	0101000020E610000007AE18A119B232401A62C00DC0C74640	ce0rEJcCcYOt8EbVlvVrIq:APA91bGi0VBtnJqbrCYFBKSoO7CJWJINGSKT8sXfBxftXcLARsRlZ3GMKx9SUA9aNAWsF7kq48nmeSZC5hylfDxGvq4mks1eBHWcuUTeg3ujLXIIwSyK0ro	Doe
95e8bd70-1073-4cd2-b474-168b632f7e2f	Lucy	0101000020E6100000D44DBDC9CAB43240E90DF7915BC74640	ce0rEJcCcYOt8EbVlvVrIq:APA91bGi0VBtnJqbrCYFBKSoO7CJWJINGSKT8sXfBxftXcLARsRlZ3GMKx9SUA9aNAWsF7kq48nmeSZC5hylfDxGvq4mks1eBHWcuUTeg3ujLXIIwSyK0ro	Donk
\.


--
-- Data for Name: rideoffer; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.rideoffer (id, "time", distance, start_location, end_location, price, confirmed, "timestamp", driver_id) FROM stdin;
62758c6e-ed83-4378-b4c7-fd7a8eba325d	4.241666666666666	1.8845	0101000020E6100000F312481ACBB3324032E8C78C1FC74640	0101000020E610000053B12A9B75B6324038B1183863C64640	3.769	t	2025-02-15 00:26:26.826647	95e8bd70-1073-4cd2-b474-168b632f7e2f
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public."user" (id, name, surname) FROM stdin;
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: driver driver_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.driver
    ADD CONSTRAINT driver_pkey PRIMARY KEY (id);


--
-- Name: rideoffer rideoffer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rideoffer
    ADD CONSTRAINT rideoffer_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: idx_driver_last_location; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_driver_last_location ON public.driver USING gist (last_location);


--
-- Name: idx_rideoffer_end_location; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_rideoffer_end_location ON public.rideoffer USING gist (end_location);


--
-- Name: idx_rideoffer_start_location; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_rideoffer_start_location ON public.rideoffer USING gist (start_location);


--
-- Name: rideoffer rideoffer_driver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rideoffer
    ADD CONSTRAINT rideoffer_driver_id_fkey FOREIGN KEY (driver_id) REFERENCES public.driver(id);


--
-- PostgreSQL database dump complete
--

