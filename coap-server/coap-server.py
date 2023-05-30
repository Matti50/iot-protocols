import requests
from os import environ

from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource


class ClimateResource(Resource):
    def __init__(self, name="ClimateResource", coap_server=None):
        super(ClimateResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Climate Resource"

    def render_GET(self, request):
        host = environ.get("INFLUX_HOST", "127.0.0.1")
        influx_url = f"http://{host}:8086/query?db=matias_cicchitti"
        query = {"q": "select * from climate"}
        res = requests.post(influx_url, data=query)
        self.payload = res.text
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = ClimateResource()
        res.location_query = request.uri_query
        host = environ.get("INFLUX_HOST", "127.0.0.1")
        influx_res = requests.post(f"http://{host}:8086/write?db=matias_cicchitti", request.payload)

        if 200 > influx_res.status_code > 299:
            res.payload = f"Error posting to influx db. Payload was: {request.payload}"
            return res

        res.payload = influx_res.text
        return res

    def render_DELETE(self, request):
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('climate/', ClimateResource())


def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()
