FROM openjdk:8-jdk
EXPOSE 8889
COPY video_proxy-0.0.1-SNAPSHOT.jar.jar /fk.jar
ENTRYPOINT ["java", "-jar", "/fk.jar"]
#pip3 install docker-compose
#docker swarm init
#docker-compose up --scale web=4 -d