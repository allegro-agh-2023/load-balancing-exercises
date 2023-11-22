package pl.edu.agh.app;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

@Controller
public class AppEndpoint {

    @RequestMapping(value = "/job", method = RequestMethod.POST)
    public ResponseEntity<JobResponse> doTheJob(@RequestBody JsonNode requestBody) throws InterruptedException {
        Thread.sleep(2000);
        return new ResponseEntity<>(new JobResponse(requestBody), HttpStatusCode.valueOf(200));
    }

    public static class JobResponse {
        private final String requestId = UUID.randomUUID().toString();
        private final JsonNode jobData;

        public JobResponse(JsonNode jobData) {
            this.jobData = jobData;
        }

        @JsonProperty("request_id")
        public String getRequestId() {
            return requestId;
        }

        @JsonProperty("job_data")
        public JsonNode getJobData() {
            return jobData;
        }
    }

    @RequestMapping(value = "/status", method = RequestMethod.GET)
    public ResponseEntity<StatusResponse> getStatus() {
        return new ResponseEntity<>(new StatusResponse(), HttpStatusCode.valueOf(200));
    }

    public static class StatusResponse {
        @JsonProperty("status")
        public String getStatus() {
            return "OK";
        }

        @JsonProperty("current_time")
        public String getCurrentTime() {
            return ZonedDateTime.now(ZoneOffset.UTC).format(DateTimeFormatter.ISO_INSTANT);
        }
    }
}
