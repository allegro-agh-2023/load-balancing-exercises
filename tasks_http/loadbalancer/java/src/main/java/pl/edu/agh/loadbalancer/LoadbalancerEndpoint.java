package pl.edu.agh.loadbalancer;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.client.RestTemplate;

import javax.servlet.http.HttpServletRequest;

@Controller
public class LoadbalancerEndpoint {

    private final RestTemplate restTemplate;

    public LoadbalancerEndpoint(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @RequestMapping(value = "/**")
    public ResponseEntity<String> balanceLoad(HttpMethod httpMethod, @RequestBody(required = false) String requestBody,
                                              @RequestHeader MultiValueMap<String, String> headers, HttpServletRequest request) {
        String firstInstanceUrl = "http://app-instance-1:5000";
        String secondInstanceUrl = "http://app-instance-2:5000";
        /*
        * If you do not use Docker, URLs look like these:
        * String firstInstanceUrl = "http://localhost:5001";
        * String secondInstanceUrl = "http://localhost:5002";
        * */

        /*
        * TODO: Start your implementation here
        *
        * Currently, all requests are forwarded to app-instance-1. Try to implement round-robin!
        * Every second request should be routed to app-instance-2.
        * You can test your load balancer with benchmark on GET http://localhost:8082/benchmark
        *
        * */

        return restTemplate.exchange(firstInstanceUrl + request.getRequestURI(), httpMethod, new HttpEntity<>(requestBody, headers), String.class);
    }
}
