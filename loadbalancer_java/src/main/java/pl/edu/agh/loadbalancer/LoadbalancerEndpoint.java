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
        String instanceUrl = "http://app-instance-1:5000";
        return restTemplate.exchange(instanceUrl + request.getRequestURI(), httpMethod, new HttpEntity<>(requestBody, headers), String.class);
    }
}
