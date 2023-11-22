FROM eclipse-temurin:17-ubi9-minimal AS TEMP_BUILD_IMAGE
WORKDIR /app
COPY . .
RUN ["./gradlew","clean","build"]

FROM eclipse-temurin:17-ubi9-minimal
WORKDIR /app
COPY --from=TEMP_BUILD_IMAGE /app/build/libs/loadbalancer-0.0.1.jar app.jar
ENTRYPOINT ["java","-jar","./app.jar"]
