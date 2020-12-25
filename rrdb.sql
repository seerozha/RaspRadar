CREATE TABLE rrsniffer_stat (
    fname varchar(255) NOT NULL,
    fdata timestamp NOT NULL,
	  fsni varchar(5) DEFAULT 'sni1im' NOT NULL, 
    fpktcount smallint
);
