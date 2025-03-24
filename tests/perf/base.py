from contextlib import contextmanager
from locust import FastHttpUser
import locust
import locust.contrib
import locust.contrib.fasthttp


class BaseDocsUser(FastHttpUser):
    abstract = True
    headers: dict | None = None

    @contextmanager
    def rest_json(self, method: str, url: str, **kwargs):
        with super().rest(method, url, headers=self.headers, **kwargs) as resp:
            if resp.js and "errorDetails" in resp.js and resp.js["errorDetails"] is not None:
                resp.failure(resp.js["errorDetails"])
            yield resp

    @contextmanager
    def rest_text(self, method: str, url: str, **kwargs):
        with self.client.request(method, url, headers=self.headers, catch_response=True, **kwargs) as resp:
            assert isinstance(resp, locust.contrib.fasthttp.ResponseContextManager)
            yield resp
