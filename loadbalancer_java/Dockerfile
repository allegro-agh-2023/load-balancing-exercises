FROM openjdk:11-slim-buster
WORKDIR /app
COPY . .
CMD ["./gradlew","clean","build"]
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","./app.jar"]
