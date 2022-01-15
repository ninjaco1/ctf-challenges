DROP DATABASE IF EXISTS ctf_league;
CREATE DATABASE ctf_league;
USE ctf_league;

CREATE TABLE challenges (
    chal_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(150),
    points INT(11),
    name VARCHAR(50),
    download VARCHAR(150),
    access VARCHAR(150),
    description VARCHAR(1000),
    category VARCHAR(20),
    release_time TIMESTAMP,
    num_weeks INT(11)
);

CREATE TABLE members (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT,
    token TEXT NOT NULL,
    verified INT(11) NOT NULL DEFAULT 0,
    is_first_blood_eligible INT(11) DEFAULT 1
);

CREATE TABLE reg_queue (
    discord_id BIGINT(20) NOT NULL PRIMARY KEY
);

CREATE TABLE reg_queue_online (
    discord_id BIGINT(20) NOT NULL PRIMARY KEY
);

CREATE TABLE solo_solves (
    solve_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    discord_id BIGINT(20) NOT NULL,
    chal_id INT(11) NOT NULL,
    submission_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE solves (
    solve_id INT(11) NOT NULL PRIMARY KEY,
    team_id INT(11) NOT NULL,
    chal_id INT(11) NOT NULL,
    submission_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_first_blood_eligible INT(11) DEFAULT 1
);

CREATE TABLE teams (
    team_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    chal_id0 INT(11) NOT NULL,
    player_0 BIGINT(20) NOT NULL,
    player_1 BIGINT(20),
    player_2 BIGINT(20),
    player_3 BIGINT(20),
    player_4 BIGINT(20),
    player_5 BIGINT(20),
    player_6 BIGINT(20),
    player_7 BIGINT(20),
    player_8 BIGINT(20),
    player_9 BIGINT(20),
    text_channel BIGINT(20),
    chal_id1 INT(11),
    chal_id2 INT(11),
    player_10 BIGINT(20),
    player_11 BIGINT(20),
    player_12 BIGINT(20),
    player_13 BIGINT(20),
    player_14 BIGINT(20),
    player_15 BIGINT(20),
    player_16 BIGINT(20),
    player_17 BIGINT(20),
    player_18 BIGINT(20),
    player_19 BIGINT(20),
    player_20 BIGINT(20)
);

CREATE TABLE users (
    discord_id BIGINT(20) NOT NULL PRIMARY KEY,
    nickname VARCHAR(20)
);

CREATE TABLE writeups (
    writeup_id INT(11) NOT NULL PRIMARY KEY,
    chal_id INT(11) NOT NULL,
    user_id BIGINT(20) NOT NULL,
    text VARCHAR(5000),
    approved TINYINT(1),
    approved_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
