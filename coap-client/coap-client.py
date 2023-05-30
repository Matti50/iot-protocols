import argparse

from coapthon.client.helperclient import HelperClient


allowed_methods = ["GET", "POST"]


argparser = argparse.ArgumentParser()

argparser.add_argument("-X", "--method", help="specify CoAP Method")
argparser.add_argument("-n", "--host", help="host IP address or DNS name. Defaults to 127.0.0.1 if not specified")
argparser.add_argument("-p", "--port", help="port number. Defaults to 5683 if not specified")
argparser.add_argument("-r", "--resource", help="the path resource you want to interact with")
argparser.add_argument("-b", "--body", help="the body payload of the request. Json format is only supported")

args = argparser.parse_args()

method = args.method

if method is None:
    print("You must specify CoAP method. Use -X")
    exit(1)

if method not in allowed_methods:
    print(f"Method {args.method} is not allowed. Allowed methods: {', '.join(allowed_methods)}")
    exit(1)

if args.resource is None:
    print("You must specify the resource you want to interact with. Use -r")
    exit(1)

host = str(args.host) if args.host is not None else "127.0.0.1"
port = args.port if args.port is not None else 5683
path = str(args.resource)

print(f"Sending {args.method} request to {host}:{port}/{path}")

client = HelperClient(server=(host, port))

if method.upper() == "GET":

    response = client.get(path)
else:
    response = client.post(path, args.body)

print(response.pretty_print())
client.stop()
