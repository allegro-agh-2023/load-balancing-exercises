FROM openjdk:11-slim-buster AS TEMP_BUILD_IMAGE
WORKDIR /app
COPY . .
RUN ["./gradlew","clean","build"]

FROM openjdk:11-slim-buster
WORKDIR /app
COPY --from=TEMP_BUILD_IMAGE /app/build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","./app.jar"]
