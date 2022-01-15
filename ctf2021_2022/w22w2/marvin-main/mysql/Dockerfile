FROM mysql:8.0

MAINTAINER me

ENV MYSQL_DATABASE=ctf_league

ADD ctf_league.sql /docker-entrypoint-initdb.d
ADD my.cnf /etc/mysql/conf.d

EXPOSE 3306
