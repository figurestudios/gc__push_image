import siaskynet as skynet
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', type=str)
parser.add_argument('-p', '--portal', type=str, default="https://siasky.net")

args = parser.parse_args()

print("portal", args.portal)
print("file", args.file)

# public portals
portals = ["http://siasky.net:80/",
           "http://web3portal.com:80/"]

print("initializing client")

client = skynet.SkynetClient(args.portal)

print("uploading file")

skylink = client.upload_file(args.file)

for portal in portals:
    print('image_url="' + portal + skylink[6:] + '",')
