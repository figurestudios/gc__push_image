import siaskynet as skynet
import argparse
import os

gvmis = []

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', type=str)
parser.add_argument('-p', '--portal', type=str, default="https://siasky.net")
parser.add_argument('-t', '--token', type=str) # you need to obtain this manually from a private/sign-up portal

# parser.add_argument('-s', '--sponsor', type=str)
# not sure if sponsored links are possible to get direct links for

args = parser.parse_args()

if args.file == None:
    files = os.listdir(os.curdir)
    for file in files:
        if file.endswith('.gvmi'):
            gvmis.append(file)
    if (str(input("Do you want continue with this file: " + gvmis[0] + " Y / N")).upper() == "Y"):
        pass
    else:
        quit()
else:
    gvmis = args.file

print("portal", args.portal)
print("file", gvmis[0])
print("token", args.token)

# public portals, required unless a token is specified
portals = ["http://siasky.net:80/",
           "http://web3portal.com:80/"]

print("initializing client")

client = skynet.SkynetClient(args.portal, {"skynet_api_key": args.token})

print("uploading file")

skylink = client.upload_file(gvmis[0])

for portal in portals:
    print('image_url="' + portal + skylink[6:] + '",')
