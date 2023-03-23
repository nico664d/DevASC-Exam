FROM ubuntu 
RUN dpkg update
RUN dpkg -i apache2 -y
RUN dpkg -i apache2-utils -y
EXPOSE 80
CMD [“apache2ctl”, “-D”, “FOREGROUND”]
